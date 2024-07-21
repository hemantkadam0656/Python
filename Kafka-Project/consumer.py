from confluent_kafka import Consumer
from configparser import ConfigParser

if __name__ == '__main__':

    config =  {
        'bootstrap.servers': 'pkc-xrnwx.asia-south2.gcp.confluent.cloud:9092',
        'sasl.username':     'HMUWQKBNVTND4VTU',
        'sasl.password':     'c7B08oKbgh1vrn3N8F+hZ3Xf/ZKhvuuza0+oEimECKAuXJc4afFo5JsrMrxludhF',

        
        'security.protocol': 'SASL_SSL',
        'sasl.mechanisms':   'PLAIN',
        'group.id':          'kafka-python-getting-started',
        'auto.offset.reset': 'earliest'
    }

    
    consumer = Consumer(config)

    topic = "PythonTopic_1"
    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                
                print("Waiting...")
            elif msg.error():
                print("ERROR: %s".format(msg.error()))
            else:
                print("Consumed event from topic {topic}: key = {key:12} value = {value:12}".format(
                    topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
                
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()