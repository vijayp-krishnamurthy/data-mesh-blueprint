from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
}

dag = DAG("transform_data", default_args=default_args, schedule_interval="@daily")

transform_task = BigQueryExecuteQueryOperator(
    task_id="run_dbt_transformation",
    sql="SELECT * FROM my_project.cleaned_table",  # Replace with actual dbt model
    use_legacy_sql=False,
    dag=dag
)
