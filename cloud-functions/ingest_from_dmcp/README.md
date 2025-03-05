```markdown
# Cloud Functions Setup

This directory contains a Cloud Function for ingesting data from DMCP BigQuery.

## Structure
- `main.py`: Cloud Function script
- `requirements.txt`: Python dependencies
- `config.json`: Configurable parameters

## Instructions
1. Modify `config.json` with your data source details.
2. Deploy the function using the following command:
   ```sh
   gcloud functions deploy ingest_from_dmcp --runtime python39 --trigger-http --allow-unauthenticated