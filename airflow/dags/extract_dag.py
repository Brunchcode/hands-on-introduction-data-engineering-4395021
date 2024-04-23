'''Extract DAG'''
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    'extract_dag',
    schedule_interval=None,
    start_date=datetime(2024,4,23),
    catchup=False
) as dag:
    
    extract_task = BashOperator(
        task_id = 'extract_task',
        bash_command='wget -c https://raw.githubusercontent.com/vinooganesh/hands-on-introduction-data-engineering-4395021-data-files/main/top-level-domain-names.csv -O /workspaces/hands-on-introduction-data-engineering-4395021/lab/orchestrated/airflow-extract-data.csv'
    )
