import sys

from confluent_kafka import Producer

if __name__ == '__main__':
    topic = "%s" % 'example1'
    conf = {
        'bootstrap.servers': 'localhost:9092',
        'session.timeout.ms': 6000,
    }

    p = Producer(**conf)

    def delivery_callback(err, msg):
        if err:
            sys.stderr.write('%% Message failed delivery: %s\n' % err)
        else:
            # sys.stderr.write('%% Message delivered to %s\n' % (msg.topic(), msg.partition()))
            sys.stderr.write('%% Message delivered: %s\n' % msg.value())

    for i in range(100):
        p.produce(topic, 'this is message %s' % i, callback=delivery_callback)
        sys.stdout.write('%% Produced: %s\n' % i)

    p.flush()