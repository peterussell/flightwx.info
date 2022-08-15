locals {
  region = "us-west-2"
}

terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws",
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "${local.region}"
}

### Modules

module "ecr" {
  source = "./modules/ecr"

  # Variables
  environment = "${var.environment}"
}

module "iam" {
  source = "./modules/iam"

  # Variables
  environment = "${var.environment}"
}
