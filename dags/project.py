from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime
from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).parent.absolute()
QUERIES_FILE = os.path.join(PROJECT_ROOT, "resources/keywords.txt")

with DAG('JarRun', description = 'Hello World DAG',

  schedule_interval = '0 0 1 * *',

  start_date=datetime(2022, 5, 15), catchup=False) as dag:

  t1 = DummyOperator(task_id = "dummy")

  t2 = BashOperator(
    task_id = 'TwitterToKafka',
    env = {"QUERIES_FILE": QUERIES_FILE},
    bash_command = 'cd ~/../../opt/airflow/dags/ && pwd && java -cp covid-tweet-analysis-assembly-0.1.0-SNAPSHOT.jar TwitterToKafka'
  )

  t3 = BashOperator(
    task_id = 'KafkaToMongo',
    bash_command = 'cd ~/../../opt/airflow/dags/ && pwd && java -cp covid-tweet-analysis-assembly-0.1.0-SNAPSHOT.jar KafkaToMongo'
  )

  t4 = BashOperator(
    task_id = 'Query5_TwitterToKafka',
    bash_command = 'cd ~/../../opt/airflow/dags/ && pwd && java -cp covid-tweet-analysis-assembly-0.1.0-SNAPSHOT.jar Query5_TwitterToKafka'
  )

  t5 = BashOperator(
    task_id = 'Query5_KafkaToMongo',
    bash_command='cd ~/../../opt/airflow/dags/ && pwd && java -cp covid-tweet-analysis-assembly-0.1.0-SNAPSHOT.jar Query5_KafkaToMongo'
  )

  t1 >> t2 >> t3 >> t4 >> t5
