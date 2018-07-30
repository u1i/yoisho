#aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,ImageId,PublicIpAddress,InstanceType,State]'
echo -e "\n------------------"
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,PublicIpAddress,InstanceType,State]' | tr -d "\n" | sed 's/"i-/#"i/g;' | tr "#" "\n"
echo -e "\n------------------"
