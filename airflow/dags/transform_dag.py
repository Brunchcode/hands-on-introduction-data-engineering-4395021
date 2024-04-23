'''Transform DAG'''
from datetime import datetime, date
from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd

with DAG(
    dag_id='transform_dag',
    schedule_interval=None,
    start_date=datetime(2024,4,23),
    catchup=False
) as dag:
    
    def transform_data():
        '''Read in the file and write the transformed file out'''
        today=date.today()
        df = pd.read_csv('/workspaces/hands-on-introduction-data-engineering-4395021/lab/orchestrated/airflow-extract-data.csv')
        generic_type_df = df[df['Type'] == 'generic']
        generic_type_df['Date'] = today.strftime('%Y-%m-%d')
        generic_type_df.to_csv('/workspaces/hands-on-introduction-data-engineering-4395021/lab/orchestrated/airflow-transform-data.csv', index = False)

    transform_task=PythonOperator(
        task_id = 'transform_task',
        python_callable=transform_data,
        dag=dag
    )

