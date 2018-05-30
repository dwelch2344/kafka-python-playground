import pickle
import string
import sys
from datetime import datetime
from random import sample

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
        rnd = ''.join(sample(string.letters, 10))
        pickled = pickle.dumps({
            "name": rnd,
            "id": i,
            "bool": True,
            "lists": [1, 2, 3],
            "date": datetime.now(),
            "floats": 1.2,
            "tuples": tuple('abc'),
            "sets": set('aaaaaabbbcc')
        })
        p.produce(topic, pickled, callback=delivery_callback)
        # sys.stdout.write('%% Produced: %s\n' % i)

    p.flush()
