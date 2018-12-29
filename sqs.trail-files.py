#!/usr/bin/env python3
#
# 2018-12

import boto3
import json
import re

get_count = 100
sqs_batch = 10

queue_name = 'myorg-cloudtrail-deliveries'

sqs     = boto3.client('sqs')
sqs_url = sqs.get_queue_url(QueueName=queue_name)['QueueUrl']


# Extract AWS region
# https://stackoverflow.com/questions/180986/what-is-the-difference-between-re-search-and-re-match
m = re.compile('_CloudTrail_(\w*-\w*-\d?)_')

for i in range(0, get_count):

    print('======================= {}'.format(i))

    # https://queue.amazonaws.com/381098461851/myorg-cloudtrail-deliveries
    # msg['Messages'][0]['Body']
    #

    # dict
    sqs_msg = sqs.receive_message(QueueUrl=sqs_url,MaxNumberOfMessages=sqs_batch)

    try:

        for s in sqs_msg['Messages']:

            # str to dict
            message = json.loads(s['Body'])['Message']

            if message == 'CloudTrail validation message.':
                print('Type: CloudTrail validation message.')
                print('Info: Event: {}, Files: {}'.format(1,0))

            else:
                print('Type: CloudTrail delivery message.')
                files = json.loads(message)['s3ObjectKey']

                delivery_event = 1
                delivery_files = len( files )
                print('Info: Event: {}, Files: {}'.format(delivery_event,delivery_files))

                for f in files:
                    filename = f.split('/')[-1]
                    delivery_region = m.search(filename).group(1)
                    print( 'File: {}|{}'.format(delivery_region,filename) )

            print('----------------------- ')

    except:
        print('Exception: \n {}'.format( str(sqs_msg)[0:40] ))
        if sqs_msg.get('ResponseMetadata'): break


print('END')

