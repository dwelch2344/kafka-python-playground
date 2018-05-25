# Kafka Python Playground


### Configuration:

1) Start Kafka: `docker-compose up -d`
2) Configure Kafka
   - Visit localhost:9000 to see the Kafka Manager
   - Add a Cluster named `sandbox` with a zookeeper host of `kafkaserver`
   - Create a topic: Topics > Create > Topic Name: `example1`
   - Assign brokers: Topics > List > Generate Partition Assignments > Click "Generate Partition Assignments"
   - TODO: more research here
3) Configure Environment:
   - Create a hosts entry for `127.0.0.1   kafkaserver` (TODO: Research why python lib expects this)
   - Install dependencies: `pip install confluent_kafka`
4) See it in action:
   - Run the producer:
     ```python producer.py```
     Notice the 100 messages are produced

   - Run the consumer:
     ```python consumer.py```
     Notice the 100 messages are consumed, and spinning occurs. CTRL + C to kill it.

   - Run the consumer again:
     ```python consumer.py```
     Notice no messages are consumed, because the brokers are tracking our offset by group

   - Run the consumer under a different group, so we get a full replay:
     ```python consumer.py -g foobarbaz```
     Notice we get all the messages again