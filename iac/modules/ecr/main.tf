resource "aws_ecr_repository" "fetcher" {
  name = "fetcher"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Environment = "${var.environment}"
  }
}

resource "aws_ecr_repository" "web" {
  name = "web"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Environment = "${var.environment}"
  }
}
