resource "aws_ecr_repository" "fetcher" {
  name = "fetcher-${var.environment}"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Environment = "${var.environment}"
  }
}

resource "aws_ecr_repository" "web" {
  name = "web-${var.environment}"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Environment = "${var.environment}"
  }
}
