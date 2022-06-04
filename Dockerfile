FROM apache/airflow:2.3.0
RUN pip install pymongo
RUN pip install quandl

COPY /dags/resources/Query_8_GDP.csv /Query_8_GDP.csv
COPY /dags/resources/countries.csv /countries.csv

USER root

RUN apt update -y && apt-get install -y software-properties-common && \
    apt-add-repository 'deb http://security.debian.org/debian-security stretch/updates main' && apt update -y && \
    apt-get install -y openjdk-8-jdk-headless && \
    export JAVA_HOME && \
    apt-get clean;

# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

USER airflow

WORKDIR /opt/airflow/dags

