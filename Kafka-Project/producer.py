from random import choice
from confluent_kafka import Producer
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

    producer = Producer(config)


    def delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
        else:
            print("Produced event to topic {topic}: key = {user_id:12} value = {product:12}".format(topic =msg.topic(),key=msg.user_id().decode('utf-8'), value = msg.product().decode('utf-8')))

    
    topic = "PythonTopic_1"
    user_ids = ["name"]
    products = ['Hemant']

    user_id = choice(user_ids)
    product = choice(products)
    producer.produce(topic, product, user_id, callback=delivery_callback)

    producer.poll(10000)
    producer.flush()