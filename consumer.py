import getopt
import sys
import pickle

from confluent_kafka import Consumer, KafkaError

if __name__ == '__main__':

    optlist, argv = getopt.getopt(sys.argv[1:], 'g:')

    consumerGroup = 'consumer1'

    for opt in optlist:
        if opt[0] == '-g':
            consumerGroup = opt[1]

    print 'Consumer group: %s' % consumerGroup

    topic = "%s" % 'example1'
    conf = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': consumerGroup,
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

        val = pickle.loads(msg.value())
        print('Received message: {}'.format(val))

    c.close()
