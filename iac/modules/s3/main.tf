resource "aws_s3_bucket" "fwx_web" {
  bucket = "${var.environment}.flightwx.info"

  tags = {
    Environment = "${var.environment}"
  }
}

resource "aws_s3_bucket_acl" "fwx_web_acl" {
  bucket = "${aws_s3_bucket.fwx_web.id}"
  acl = "public-read"
}

resource "aws_s3_bucket_website_configuration" "fwx_web_website_configuration" {
  bucket = "${aws_s3_bucket.fwx_web.bucket}"

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "error.html"
  }
}
