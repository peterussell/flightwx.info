resource "aws_iam_user" "github_deployer" {
  name = "github_deployer"
  
  tags = {
    Environment = "${var.environment}"
  }
}

resource "aws_iam_access_key" "github_deployer_access_key" {
  user = "${aws_iam_user.github_deployer.name}"
}

resource "aws_iam_user_policy" "github_deployer_policy" {
  name = "github_deployer_policy"
  user = "${aws_iam_user.github_deployer.name}"

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "ecr:*"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
EOF
}

output "github_deployer_secret" {
  value = "${aws_iam_access_key.github_deployer_access_key.encrypted_secret}"
}