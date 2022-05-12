from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime,timedelta

with DAG('aaaaaASCII', description='Hello World DAG',
  schedule_interval='* * * * *',
  start_date=datetime(2022, 3, 20), catchup=False) as dag:
  t1 = DummyOperator(task_id = "dummy")
#   t2 = DummyOperator(task_id = "dummy2")

  t2 = BashOperator(
    task_id = 'jar_run', bash_command = 'java -cp scala-spark_2.13-0.1.0-SNAPSHOT.jar check1'
  )
  t1>>t2
