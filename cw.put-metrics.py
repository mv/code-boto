#!/usr/bin/env python3
#
# 2018-12

import boto3
import random

# for x in range(10):
#   print(random.randint(1,101))

vmin = 0
vmax = 100

# 0: do not stop
counter = 5

queue_name = 'myorg-cloudtrail-deliveries'

sqs     = boto3.client('sqs')
sqs_url = sqs.get_queue_url(QueueName=queue_name)['QueueUrl']

# "Timestamp" : "2018-12-26T18:52:46.218Z"
#  print( datetime.strftime( datetime.today(), '%Y-%m-%dT%H:%M:%S.%f') )
#  print( datetime.strftime( datetime.today(), '%Y-%m-%dT%H:%M:%S.%X') )
#  https://stackoverflow.com/questions/41726845/convert-zulu-time-string-to-mst-datetime-object

datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

count=1
while True:

    val = random.randint(vmin,vmax)
    MetricData = [{
        'MetricName': 'Deliveries',
        'Dimensions': [ { 'Name': 'Region', 'Value': 'us-east-1' }, ],
        'Timestamp': datetime(2015, 1, 1),
        'Value': val,
        'Unit': 'Count'
    }]

    response = 1 #cw.put_metric_data(Namespace='CWTest', MetricData )

    print('===== {}: {} {}'.format(count,val,response))

    count+=1
    if   counter == 0: continue     # do not stop
    elif count > counter: break


print('End')

