from airflow import DAG
from airflow.providers.google.cloud.operators.functions import CloudFunctionInvokeFunctionOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator
from airflow.providers.google.cloud.operators.dagrun import TriggerDagRunOperator
from datetime import datetime

PROJECT_ID = "my-gcp-project"
DATASET_ID = "processed_data"
TABLE_ID = "cleaned_table"

default_args = {
    "start_date": datetime(2024, 1, 1),
}

with DAG("ingest_data_dag", schedule_interval="0 12 * * *", default_args=default_args, catchup=False) as dag:

    ingest_data = CloudFunctionInvokeFunctionOperator(
        task_id="call_ingest_function",
        project_id=PROJECT_ID,
        location="us-central1",
        function_name="ingest-from-dmcp",
        data={
            "source_project": "dmcp_project",
            "source_dataset": "dmcp_dataset",
            "source_table": "dmcp_table",
            "dest_project": PROJECT_ID,
            "dest_dataset": DATASET_ID,
            "dest_table": TABLE_ID,
        }
    )

    run_dbt = TriggerDagRunOperator(
        task_id="trigger_dbt_dag",
        trigger_dag_id="dbt_transform_dag"
    )

    ingest_data >> run_dbt
