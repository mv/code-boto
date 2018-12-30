#!/usr/bin/env python3
#
# 2018-12

import boto3
import random
import datetime as dt
import time

vmin = 0
vmax = 100

# 0: do not stop
counter = 5

cw = boto3.client('cloudwatch')

# "Timestamp" : "2018-12-26T18:52:46.218Z"
#  https://stackoverflow.com/questions/41726845/convert-zulu-time-string-to-mst-datetime-object
#
#  iso_8601_str = '2018-12-26T18:52:46.218Z'
#  iso_8601_dt  = dt.datetime.strptime(iso_8601_str[:-1], '%Y-%m-%dT%H:%M:%S.%f')
#  iso_8601_tms = iso_8601_dt.timestamp()
#
#  iso_8601  = '2018-12-26T18:52:46.218Z'
#  timestamp = dt.datetime.strptime(iso_8601[:-1], '%Y-%m-%dT%H:%M:%S.%f').timestamp()


count=1
while True:

    val = random.randint(vmin,vmax)
    tms = dt.datetime.now().timestamp()

    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_data
    metric = [{
        'MetricName': 'Deliveries',
        'Dimensions': [ { 'Name': 'Region', 'Value': 'us-east-1' }, ],
        'Timestamp':  tms,
        'Value':      val,
        'Unit':       'Count'
    }]

    res  = cw.put_metric_data(Namespace='CWTest', MetricData=metric)
    code = response['ResponseMetadata']['HTTPStatusCode']

    print( '===== {}: {} {} {}'.format(count,val,tms,code) )
    time.sleep(5)

    count+=1
    if   counter == 0: continue     # do not stop
    elif count > counter: break     # stop when reaching counter

# end while

print('End')

