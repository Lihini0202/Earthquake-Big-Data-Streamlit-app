terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# 1. A NEW Resource Group for the Earthquake App
resource "azurerm_resource_group" "earthquake_rg" {
  name     = "earthquake-predictor-rg" # New, unique name!
  location = var.region
}

# 2. A NEW Container Registry for the Earthquake App
resource "azurerm_container_registry" "earthquake_acr" {
  name                = "earthquakeacr${random_id.acr_suffix.hex}" # New name!
  resource_group_name = azurerm_resource_group.earthquake_rg.name
  location            = azurerm_resource_group.earthquake_rg.location
  sku                 = "Basic"
  admin_enabled       = true
}

resource "random_id" "acr_suffix" {
  byte_length = 4
}

# 3. The Earthquake App Itself
resource "azurerm_container_group" "earthquake_app" {
  name                = "earthquake-app-instance"
  location            = azurerm_resource_group.earthquake_rg.location
  resource_group_name = azurerm_resource_group.earthquake_rg.name
  os_type             = "Linux"
  ip_address_type     = "Public" 

  image_registry_credential {
    server   = azurerm_container_registry.earthquake_acr.login_server
    username = azurerm_container_registry.earthquake_acr.admin_username
    password = azurerm_container_registry.earthquake_acr.admin_password
  }

  container {
    name   = "earthquake-dashboard-container"
    # This DYNAMICALLY uses the new registry we just defined!
    image  = "${azurerm_container_registry.earthquake_acr.login_server}/earthquake-dashboard:latest"
    cpu    = 1
    memory = 2
    ports {
      port     = 8501
      protocol = "TCP"
    }
  }
}

# 4. Outputs
output "earthquake_acr_name" {
  value = azurerm_container_registry.earthquake_acr.name
}

output "earthquake_app_url" {
  value = "http://${azurerm_container_group.earthquake_app.ip_address}:8501"
}
