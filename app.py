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
print(df.head())
df = df.set_index('Date_Time')
df['Duration'] = pd.to_timedelta(df.Duration)
df.index = pd.to_datetime(df.index)
# df.to_dict('index')
tinder = df[df['App name'] == 'Tinder']
# grouped = df.groupby('App name')

tinder = tinder.resample('H')['Duration'].sum().reset_index()
tinder.Duration = pd.to_datetime(tinder['Date_Time'].dt.date.astype(str) + ' ' + tinder['Duration'].dt.to_pytimedelta().astype(str))


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)


@app.route("/")
def chart():
    # obj = json.dumps(dates, cls=DateTimeEncoder)
    chart = alt.Chart(tinder).mark_bar().encode(
        #     x='day(Date):O',
        x='Date_Time:T',
        y='hoursminutes(Duration)'
    ).interactive()

    return chart.to_json()  # dates.to_html()


if __name__ == "__main__":
    app.run(debug=True)
