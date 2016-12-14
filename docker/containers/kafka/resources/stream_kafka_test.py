

import os,sys,re,csv
import datetime,time
import random
from kafka import KafkaProducer

try:
   data_file = sys.argv[1]
except:
   data_file   = '/mosaic_data_test.csv'

#data_file   = '/mosaic_data.csv' 
#brokers     = ['seregion03.cloud.hortonworks.com:6667','seregion04.cloud.hortonworks.com:6667']
#brokers     = ['sandbox.hortonworks.com:6667']
brokers     = ['kafka.dev:9092']
topic       = 'dztopic1'

#producer = KafkaProducer(bootstrap_servers=brokers, value_serializer=lambda m: json.dumps(m).encode('ascii'))
producer = KafkaProducer(bootstrap_servers=brokers)
file     = csv.reader(open(data_file, 'rb'))
header   = file.next()

for i,row in enumerate(file):
    time.sleep(0.5)
    record = '|'.join(row)
    print str(record)
    producer.send(topic, record)
    if i==8:
        time.sleep(12)

#ZEND
