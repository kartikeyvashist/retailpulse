from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG(
    'retailpulse_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False
)

task_db = BashOperator(
    task_id='create_tables',
    bash_command='python /opt/airflow/dags/db.py',
    dag=dag
)

task_ingest = BashOperator(
    task_id='ingest_data',
    bash_command='python /opt/airflow/dags/ingestion.py',
    dag=dag
)

task_dbt_run = BashOperator(
    task_id='dbt_run',
    bash_command='cd /opt/airflow/dags/retailpulse_dbt/ && dbt run',
    dag=dag
)

task_analysis = BashOperator(
    task_id='analyze_data',
    bash_command='python /opt/airflow/dags/analysis.py',
    dag=dag
)

task_dbt_test = BashOperator(
    task_id='dbt_test',
    bash_command='cd /opt/airflow/dags/retailpulse_dbt && dbt test',
    dag=dag
)

task_db >> task_ingest >> task_dbt_run >> task_dbt_test >> task_analysis