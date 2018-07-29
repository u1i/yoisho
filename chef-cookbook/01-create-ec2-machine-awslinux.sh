# Needs aws cli setup with the files $HOME/.aws/credentials and $HOME/.aws/config (optional)
# Values are good for AWS region = ap-southeast-1

# Amazon Linux 2 
ami=ami-05868579

# Subnet
subnet=subnet-8c9e55e9

# Instance Type
itype=t2.micro

# SSH Key
sshkey=uh-2017-06

# Security Group
sec=sg-1a2ee67f

aws ec2 run-instances --image-id $ami --count 1 --instance-type $itype --key-name $sshkey --security-group-ids $sec --subnet-id $subnet --associate-public-ip-address

