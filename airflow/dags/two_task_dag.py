'''Two task DAG'''
from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Anthony',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retries': False,
    'retries': 0,
    'catchup': False,
    'start_date': datetime(2024,4,22)
}

with DAG(
    dag_id='two_task_dag',
    description='Running a two task dag',
    schedule_interval=None,
    default_args=default_args
) as dag:
    
    t0 = BashOperator(
        task_id = 'Bash_task_0',
        bash_command='echo "First airflow task"'
    )

    t1 = BashOperator(
        task_id = 'Bash_task_1',
        bash_command='echo "Sleeping..." && sleep 5s && echo "second airflow task"'
    )

    t0 >> t1