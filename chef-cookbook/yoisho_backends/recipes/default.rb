#
# Cookbook:: yoisho_backends
# Recipe:: default
#
# Author: Uli Hitzel - uli.hitzel@gmail.com

# Install Docker
docker_installation 'default'

# Currency
docker_image 'u1ih/yoisho-currency' do
  tag 'latest'
  action :pull
  notifies :redeploy, 'docker_container[yoishocurrency]'
end

docker_container 'yoishocurrency' do
  repo 'u1ih/yoisho-currency'
  tag 'latest'
  port '8080:8080'
end
