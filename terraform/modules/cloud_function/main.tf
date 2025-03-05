resource "google_storage_bucket" "function_bucket" {
  name          = "${var.project_id}-functions"
  location      = var.region
  force_destroy = true
}

resource "google_storage_bucket_object" "function_zip" {
  name   = "ingest_from_dmcp.zip"
  bucket = google_storage_bucket.function_bucket.name
  source = "${path.module}/ingest_from_dmcp.zip"
}

resource "google_cloudfunctions_function" "ingest_from_dmcp" {
  name                  = "ingest-from-dmcp"
  runtime               = "python311"
  available_memory_mb   = 256
  source_archive_bucket = google_storage_bucket.function_bucket.name
  source_archive_object = google_storage_bucket_object.function_zip.name
  entry_point           = "ingest_data"
  trigger_http          = true
  timeout               = 60

  environment_variables = {
    BQ_PROJECT   = var.bq_project
    BQ_DATASET   = var.bq_dataset
    BQ_TABLE     = var.bq_table
  }
}
