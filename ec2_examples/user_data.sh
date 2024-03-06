#!/bin/bash -xe
# Install Apache web server
# e ->exit immediately exit immediately if any command exits with a non-zero status
# x ->each command in the script will be printed to the console
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<html><body><h1>Hello World from the instance $(hostname -f)</h1></body></html>" > /var/www/html/index.html
