from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def extract_from_api():
    print("Extracting from API")


def land_to_object_storage():
    print("Landing to object storage")


def load_warehouse():
    print("Loading to warehouse")


def dbt_run():
    print("Running dbt")


def dbt_test():
    print("Testing dbt")


with DAG(
    dag_id="practical_exam",
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id="extract_task",
        python_callable=extract_from_api,
    )

    land_task = PythonOperator(
        task_id="land_task",
        python_callable=land_to_object_storage,
    )

    load_task = PythonOperator(
        task_id="load_task",
        python_callable=load_warehouse,
    )

    dbt_run_task = PythonOperator(
        task_id="dbt_run_task",
        python_callable=dbt_run,
    )

    dbt_test_task = PythonOperator(
        task_id="dbt_test_task",
        python_callable=dbt_test,
    )

    extract_task >> land_task >> load_task >> dbt_run_task >> dbt_test_task
