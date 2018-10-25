import pandas as pd
import pymysql


REGION = 'us-east-1'

rds_host = "apptracker.cx9kixeir2qg.us-east-1.rds.amazonaws.com"
username = "$(USERNAME)"
password = "$(PASSWORD)"
db_name = "$(DB_NAME)"


def get_filename(event, context):
    print("Loading bucket")
    bucket = event['Records'][0]['s3']['bucket']['name']
    filename = event['Records'][0]['s3']['object']['key']
    print("bucket: ", bucket)
    print("filename: ", filename)

    return filename


def transform_table(file):
    """
    This function simplifies the table structure and bins app usage by the hour
    """
    df = pd.read_csv(file, parse_dates=[['Date', 'Time']])
    df = df[:-3]
    df = df.set_index('Date_Time')
    df['Duration'] = pd.to_timedelta(df.Duration)
    df.index = pd.to_datetime(df.index)
    df['App name'] = df['App name'].astype(str)
    print(df.dtypes)

    df = df.resample('H')['Duration'].sum().reset_index()
    print(df.head())
    df.Duration = pd.to_datetime(df['Date_Time'].dt.date.astype(str) + ' ' + df['Duration'].dt.to_pytimedelta().astype(str))
    print(df.head())

    return df


def save_events(event):
    """
    This function fetches content from mysql RDS instance
    """
    result = []
    conn = pymysql.connect(rds_host, user=username, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
        cur.execute("""insert into test (id, name) values( %s, '%s')""" % (event['id'], event['name']))
        cur.execute("""select * from test""")
        conn.commit()
        cur.close()
        for row in cur:
            result.append(list(row))
        print("Data from RDS...")
        print(result)


def main(event, context):
    file = get_filename(event, context)
    df = transform_table(file)
    save_events(event, df)
