ip=$1
nodename=node${RANDOM}-ubuntu
sshuser=ubuntu
ssh_key=$HOME/.ssh/uh-2017-06.pem

knife bootstrap $ip --ssh-user $sshuser --sudo --identity-file $ssh_key --node-name $nodename --run-list 'recipe[yoisho_backends]'

knife node show $nodename
