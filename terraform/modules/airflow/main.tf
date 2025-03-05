resource "google_composer_environment" "airflow" {
  name    = "airflow-${var.environment}"
  project = var.project_id
  region  = var.region

  config {
    node_count = 3

    software_config {
      image_version = "composer-2.1.0-airflow-2.5.1"
      env_variables = {
        GCP_PROJECT = var.project_id
      }
    }
  }
}
