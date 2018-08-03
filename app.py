import pandas as pd
import sys
import altair as alt
from vega_datasets import data


data_path = 'data/AUM_V4_Activity_2018-06-21_17-16-27.csv'
# with open(data_path) as f:
#     for line in f:
#         print(line)

df = pd.read_csv(data_path)
df = df[:-3]

alt.Chart(df).mark_point().encode(
    x='App name',
    y='Date'
)

cars = data.cars()

chart = alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
)

print(chart)
