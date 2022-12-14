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

  assume_role {
    role_arn = "${var.deployer_role_arn}"
  }
}

### Modules

module "ecr" {
  source = "./modules/ecr"
  environment = "${var.environment}"
}

module "iam" {
  source = "./modules/iam"
  environment = "${var.environment}"
}

module "s3" {
  source = "./modules/s3"
  environment = "${var.environment}"
}
