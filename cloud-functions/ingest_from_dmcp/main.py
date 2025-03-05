import functions_framework
from google.cloud import bigquery

# Initialize BigQuery client
bq_client = bigquery.Client()

@functions_framework.http
def ingest_data(request):
    """Ingest data from DMCP BigQuery to another BigQuery table."""
    request_json = request.get_json()
    
    source_project = request_json.get("source_project")
    source_dataset = request_json.get("source_dataset")
    source_table = request_json.get("source_table")
    
    dest_project = request_json.get("dest_project")
    dest_dataset = request_json.get("dest_dataset")
    dest_table = request_json.get("dest_table")
    
    query = f"""
        INSERT INTO `{dest_project}.{dest_dataset}.{dest_table}`
        SELECT * FROM `{source_project}.{source_dataset}.{source_table}`;
    """
    
    query_job = bq_client.query(query)
    query_job.result()  # Wait for job to complete
    
    return "Data ingested successfully!", 200
