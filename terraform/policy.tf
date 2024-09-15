data "google_iam_policy" "noauth" {
  binding {
    role    = "roles/run.invoker"
    members = ["allUsers"]
  }
}

resource "google_cloud_run_service_iam_policy" "noauth_api" {
  location    = "southamerica-east1"
  project     = "pyservice-project"
  service     = "pyservice"
  policy_data = data.google_iam_policy.noauth.policy_data
  depends_on  = [google_cloud_run_v2_service.pyservice]
}
