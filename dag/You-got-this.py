from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from includes.Abhi_modules.test import hello
from includes.Abhi_modules.test2 import see

#https://www.youtube.com/watch?v=IsWfoXY_Duk

args = {
    'owner': 'Abhinaya',
    'start_date': days_ago(1) # make start date in the past
}

dag = DAG(
    dag_id='You-got-this',
    default_args=args,
    schedule_interval='@daily' # make this workflow happen every day
)

with dag:
    hello_world = PythonOperator(
        task_id='hello',
        python_callable=hello,
        # provide_context=True
    )

with dag:
    hello_world = PythonOperator(
        task_id='see',
        python_callable=see,
        # provide_context=True
    )
