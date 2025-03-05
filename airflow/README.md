```markdown
# Airflow Setup

This directory contains Apache Airflow DAGs and configurations.

## Structure
- `dags/`: DAGs for orchestration
  - `ingest_data.py`: DAG for ingestion
  - `transform_data.py`: DAG for dbt transformations
  - `pipeline.py`: Full pipeline DAG
- `plugins/`: Custom operators/hooks
- `requirements.txt`: Python dependencies for Airflow

## Instructions
1. Install dependencies:
   ```sh
   pip install -r requirements.txt