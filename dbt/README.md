```markdown
# dbt Setup

This directory contains dbt models and configurations for data transformations.

## Structure
- `models/`: dbt models (staging, intermediate, marts)
- `tests/`: Data quality tests
- `dbt_project.yml`: dbt project config

## Instructions
1. Update `dbt_project.yml` with your project details.
2. Run the following commands to validate data transformations:
   ```sh
   dbt run
   dbt test