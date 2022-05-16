FROM apache/airflow:2.3.0

USER root

# Install OpenJDK-11
# RUN apt update && \
#     apt-get install -y openjdk-11-jdk && \
#     apt-get install -y ant && \
#     apt-get clean;


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

# # Set JAVA_HOME
# ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
# RUN export JAVA_HOME

USER airflow

WORKDIR /opt/airflow/dags

