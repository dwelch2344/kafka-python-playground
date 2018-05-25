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
4) Run it:
   - python producer.py