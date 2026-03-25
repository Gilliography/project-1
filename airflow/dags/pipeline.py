from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="data_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@hourly",
    catchup=False
) as dag:

    start_producer = BashOperator(
        task_id="run_producer",
        bash_command="python /opt/airflow/streaming/producer.py"
    )

    run_spark = BashOperator(
        task_id="run_spark",
        bash_command="python /opt/airflow/streaming/consumer_spark.py"
    )

    transform = BashOperator(
        task_id="run_sql",
        bash_command="psql -U user -d rides -f /opt/airflow/batch/transformations.sql"
    )

    start_producer >> run_spark >> transform