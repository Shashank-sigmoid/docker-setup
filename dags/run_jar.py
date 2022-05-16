from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime,timedelta

with DAG('JarRun', description='Hello World DAG',
  schedule_interval='0 0 1 * *',
  start_date=datetime(2022, 5, 15), catchup=False) as dag:
  t1 = DummyOperator(task_id = "dummy")
#   t2 = DummyOperator(task_id = "dummy2")

  t3 = BashOperator(
    task_id = 'directory_find', bash_command = 'cd ~/../../opt/airflow/dags/ && pwd && java -cp covid-tweet-analysis-assembly-0.1.0-SNAPSHOT.jar TwitterToKafka'
  )

  # t4 = BashOperator(
  #   task_id = 'directory_find', bash_command = 'pwd'
  # )

  # t2 = BashOperator(
  #   task_id = 'jar_run', bash_command = 'java -cp covid-tweet-analysis-assembly-0.1.0-SNAPSHOT.jar TwitterToKafka'
  # )
  t1>>t3
