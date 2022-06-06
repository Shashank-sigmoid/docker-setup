# Docker Setup

### Docker-compose configuration

### Follow this [Link](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html#)

1. Install Docker Community Edition (CE) for your workstation. <br/>
Install Docker Compose on your workstation.<br/>

To check the versions installed in your system:
```bash
docker --version
docker-compose --version
```

To deploy Airflow on Docker Compose, fetch docker-compose.yaml
```bash
curl -LFO 'https://github.com/GeoscienceAustralia/dea-airflow/blob/master/docker-compose.workflow.yaml'
```

Initializing the Environment:
```bash
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

Initializing the database:
```bash
docker-compose up airflow-init
```

Start all services:
```bash
docker-compose up
```

ID: airflow <br/>
Password: airflow

### Follow this [Link](https://github.com/wurstmeister/kafka-docker/blob/master/docker-compose.yml) 

2. Add Kafka and Zookeeper images in services in docker-compose.yaml file. <br/>
Specify the ports correctly. <br/><br/>

3. To check if Kafka is working fine:
```bash
docker exec -it <kafka_container_name> /bin/sh
cd opt/kafka
```

To create Kafka-topics:
```bash
bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic covid-tweet
```

To list the Kafka-topics:
```bash
bin/kafka-topics.sh --list --zookeeper zookeeper:2181
```

To send messages from the console-producer
```bash
bin/kafka-console-producer.sh --broker-list kafka:9092 --topic covid-tweet
```

To fetch the messages in console-consumer
```bash
bin/kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic covid-tweet --from-beginning
```

4. Add MongoDB image in services in docker-compose.yaml file.<br/>

To check if MongoDB is working fine, connect to the server:
```bash
docker exec -it <MongoDB_container_name> /bin/sh
mongo --host localhost:27017 -u <user_name> -p <password>
```

To list all the databases present:
```bash
show dbs
```

### Dockerfile configuration

1. Install the required libraries
```bash
RUN pip install pymongo
RUN pip install quandl
```

2. Copy the required files in the Airflow
```bash
COPY /dags/resources/Query_8_GDP.csv /Query_8_GDP.csv
COPY /dags/resources/countries.csv /countries.csv
```

### DAG file configuration

1. Import all the airflow utilities and query files
2. Create tasks to run the queries
3. Schedule the DAG with schedule_interval

### Tasks configuration

1. To run the scala file present in the JAR
```bash
t = BashOperator(
        task_id="task_id",
        bash_command='cd ~/../../opt/airflow/dags/ && pwd && java -cp <JAR_filename> <Scala_filename>'
```

2. To run the python scripts as tasks
```bash
t = PythonOperator(
        task_id="task_id",
        python_callable=python_func
    )
```

