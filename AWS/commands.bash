# ------------------------------
# AWS
# ------------------------------



aws --version
# configure account
aws configure 
aws configure list
# see if everything is working
aws sts get-caller-identity
aws ec2 describe-vpcs
aws ec2 describe-instances

aws s3 ls


### 
# ADD AUtompletion
# https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-completion.html
###

vim ~/.bashrc
complete -C '/usr/local/bin/aws_completer' aws


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


