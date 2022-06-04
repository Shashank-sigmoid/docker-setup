# Docker Setup


1. Follow this [Link](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html#docker-compose-env-variables)
```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.3.0/docker-compose.yaml'
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
docker-compose up airflow-init
docker-compose up
```
2. Now to check kafka is up or not

```bash
docker exec -it [kafka_container_name] /bin/sh
cd opt/kafka_2.13-2.8.1/bin/
kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic first_kafka_topic
kafka-topics.sh --list --zookeeper zookeeper:2181
```