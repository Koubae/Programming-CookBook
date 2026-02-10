# ------------------------------
# AWS
# ------------------------------



aws --version
# configure account
aws configure 
# see if everything is working
aws ec2 describe-vpcs
aws ec2 describe-instances

aws s3 ls


# how to get the right platform name - eg. 64bit Amazon Linux 2 v5.4.4 running Node.js 14
aws elasticbeanstalk list-available-solution-stacks


# ------------------------------
# AWS CDK
# https://docs.aws.amazon.com/cdk/v2/guide/cli.html
# ------------------------------
# Install cdk globally (using node)
npm install -g aws-cdk
cdk --version

# Bootstrapping your AWS Account
# Get the account ID
aws sts get-caller-identity

# Bootstrap the account
cdk bootstrap aws://ACCOUNT-NUMBER/REGION
# for london https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html
cdk bootstrap aws://ACCOUNT-NUMBER/eu-west-2


