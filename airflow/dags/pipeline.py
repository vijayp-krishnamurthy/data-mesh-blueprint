from airflow import DAG
from airflow.operators.http_operator import SimpleHttpOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
from airflow.utils.dates import days_ago
from airflow.operators.email_operator import EmailOperator

default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
}

dag = DAG("full_pipeline", default_args=default_args, schedule_interval="@daily")

ingest_task = SimpleHttpOperator(
    task_id="call_ingest_function",
    method="POST",
    http_conn_id="cloud_function_ingest",
    endpoint="/",
    dag=dag
)

transform_task = BigQueryExecuteQueryOperator(
    task_id="run_dbt_transformation",
    sql="SELECT * FROM my_project.cleaned_table",  # Replace with actual dbt model
    use_legacy_sql=False,
    dag=dag
)

notify_task = EmailOperator(
    task_id="send_notification",
    to="team@example.com",
    subject="Pipeline Success",
    html_content="Pipeline executed successfully!",
    dag=dag
)

ingest_task >> transform_task >> notify_task
