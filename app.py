from flask import Flask, render_template
import pandas as pd
import altair as alt
from vega_datasets import data
from datetime import datetime
import json


app = Flask(__name__)

data_path = 'data/AUM_V4_Activity_2018-06-21_17-16-27.csv'

df = pd.read_csv(data_path, parse_dates=[['Date', 'Time']])
df = df[:-3]
df = df.set_index('Date_Time')
df['Duration'] = pd.to_timedelta(df.Duration)
df.index = pd.to_datetime(df.index)

# tinder = df[df['App name'] == 'Tinder']
# tinder = tinder.resample('H')['Duration'].sum().reset_index()
# tinder.Duration = pd.to_datetime(tinder['Date_Time'].dt.date.astype(str) + ' ' + tinder['Duration'].dt.to_pytimedelta().astype(str))
# print(tinder.head())

df = df.resample('H')['Duration'].sum().reset_index()
print(df.head())
df.Duration = pd.to_datetime(df['Date_Time'].dt.date.astype(str) + ' ' + df['Duration'].dt.to_pytimedelta().astype(str))
print(df.head())


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)


@app.route("/", methods=["GET"])
def main():
    return render_template('index.html')


@app.route("/data/bar")
def chart():
    # obj = json.dumps(dates, cls=DateTimeEncoder)
    chart = alt.Chart(tinder).mark_bar().encode(
        #     x='day(Date):O',
        x='Date_Time:T',
        y='hoursminutes(Duration)'
    )

    return chart.to_json()  # dates.to_html()


if __name__ == "__main__":
    app.run(debug=True, threaded=True, port=8080)
