import sys

from confluent_kafka import Consumer, KafkaError, TopicPartition, OFFSET_BEGINNING

if __name__ == '__main__':
    topic = "%s" % 'example1'
    conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'consumer1',
        'default.topic.config': {'auto.offset.reset': 'smallest'}
    }

    c = Consumer(conf)
    c.subscribe([topic])
    # c.seek(TopicPartition(topic, 0, OFFSET_BEGINNING))



    print("About to start...")
    while True:
        print("Reading...")
        msg = c.poll(1.0)
        if msg is None:
            print("No message...")
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("EOF...")
                continue
            else:
                print(msg.error())
                break

        print('Received message: {}'.format(msg.value().decode('utf-8')))

    c.close()