# Importing airflow utilities
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
from pathlib import Path
import os

# Importing queries
from Queries.query_6 import query_6
from Queries.query_7 import query_7
from Queries.query_8 import query_8

# Importing date conversion
from Date_conversion.date_conversion import date_conversion
from Date_conversion.donations_date import donations_date

# Importing summary tables
from Summary_table.summary_table1 import summary_table1
from Summary_table.summary_table2 import summary_table2

PROJECT_ROOT = Path(__file__).parent.absolute()
QUERIES_FILE = os.path.join(PROJECT_ROOT, "resources/keywords.txt")

with DAG("ProjectRun", description="Hello World DAG",

         schedule_interval="0 0 1 * *",

         start_date=datetime(2022, 5, 25), catchup=False) as dag:

    t1 = DummyOperator(task_id="DummyOperator")

    t2 = BashOperator(
        task_id="TwitterToKafka",
        env={"QUERIES_FILE": QUERIES_FILE},
        bash_command='cd ~/../../opt/airflow/dags/ && pwd && java -cp '
                     'covid-tweet-analysis-assembly-0.1.0-SNAPSHOT.jar TwitterToKafka '
    )

    t3 = BashOperator(
        task_id='KafkaToMongo',
        bash_command='cd ~/../../opt/airflow/dags/ && pwd && java -cp '
                     'covid-tweet-analysis-assembly-0.1.0-SNAPSHOT.jar KafkaToMongo '
    )

    t4 = BashOperator(
        task_id='Query5_TwitterToKafka',
        bash_command='cd ~/../../opt/airflow/dags/ && pwd && java -cp '
                     'covid-tweet-analysis-assembly-0.1.0-SNAPSHOT.jar Query5_TwitterToKafka '
    )

    t5 = BashOperator(
        task_id='Query5_KafkaToMongo',
        bash_command='cd ~/../../opt/airflow/dags/ && pwd && java -cp '
                     'covid-tweet-analysis-assembly-0.1.0-SNAPSHOT.jar Query5_KafkaToMongo '
    )

    t6 = PythonOperator(
        task_id="Query_6",
        python_callable=query_6
    )

    t7 = PythonOperator(
        task_id="Query_7",
        python_callable=query_7
    )

    t8 = PythonOperator(
        task_id="Query_8",
        python_callable=query_8
    )

    t9 = PythonOperator(
        task_id="Date_conversion_tweets",
        python_callable=date_conversion
    )

    t10 = PythonOperator(
        task_id="Date_conversion_donations",
        python_callable=donations_date
    )

    t11 = PythonOperator(
        task_id="Summary_table1",
        python_callable=summary_table1
    )

    t12 = PythonOperator(
        task_id="Summary_table2",
        python_callable=summary_table2
    )

    t1 >> t2 >> t3 >> t4 >> t5 >> t9 >> t11 >> t12
    t7
    t8
    t6 >> t10

