# apptracker
Dynamic web app that graphs my app usage behavior trends

## Current State
A series of jupyter notebooks documenting my sandbox learning approach of pandas and altair

## TODO
### Phase 1 (in progress)
Round out my knowledge of pandas dataframes and altair to create a chart that shows the weekly view of one app's cumulative hours opened per hour.

### Phase 2
Add a route to a Flask app that allows the chart to be displayed in the browser

### Phase 3
Use Zappa to push app to Lambda

### Phase 4
Make endpoint in AWS Route 53, store CSV and index.html in S3, and connect to single Lambda function to create the chart

### Phase 5
Create one Lambda function (Triggered by Route 53) that processes data from S3 and saves it to RDS. Another Lambda function trigger displays the chart.
