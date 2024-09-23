resource "google_cloud_run_v2_service" "pyservice" {
  name     = "pyservice"
  location = "southamerica-east1"
  ingress  = "INGRESS_TRAFFIC_INTERNAL_LOAD_BALANCER"
  
  template {
    containers {
      image = "southamerica-east1-docker.pkg.dev/pyservice-project/pyservice/pyservice:latest"
      
      resources {
        cpu_idle = true
        
        limits = {
          cpu    = "2"
          memory = "1536Mi"
        }
        
        startup_cpu_boost = false
      }
      
      ports {
        container_port = 9101
      }
      
      volume_mounts {
        mount_path = "/cloudsql"
        name       = "cloudsql"
      }
      
       env {
         name  = "GCP:Token"
         value = "some-token-example"
       }
     }
    
    scaling {
      max_instance_count = 4
      min_instance_count = 0
    }
    
    volumes {
      name = "cloudsql"
      cloud_sql_instance {
        instances = [
          "pyservice-project:southamerica-east1:pyservice-database",
        ]
      }
    }

    vpc_access {
      network_interfaces {
        network    = "pyservice-vpc"
        subnetwork = "pyservice-subnet-sa-east1-a"
        tags       = ["private"]
      }
    }
  }
}
