resource "google_storage_bucket" "dbt_bucket" {
  name          = "${var.project_id}-dbt"
  location      = var.region
  force_destroy = true
}

resource "google_storage_bucket_object" "dbt_project" {
  name   = "dbt_project.zip"
  bucket = google_storage_bucket.dbt_bucket.name
  source = "${path.module}/dbt_project.zip" # Zip of dbt project
}
