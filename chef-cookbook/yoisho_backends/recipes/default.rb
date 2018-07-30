#
# Cookbook:: yoisho_backends
# Recipe:: default
#
# Author: Uli Hitzel - uli.hitzel@gmail.com

# Install Docker
docker_installation 'default'

# Enable the Docker service

docker_service_manager 'default' do
  action :start
end

# Currency REST API
docker_image 'u1ih/yoisho-currency' do
  tag 'latest'
  action :pull
  notifies :redeploy, 'docker_container[yoishocurrency]'
end

docker_container 'yoishocurrency' do
  repo 'u1ih/yoisho-currency'
  tag 'latest'
  port "#{node["yoisho"]["currency_port"]}:8080"
end

# Bank Assets SOAP Service
docker_image 'u1ih/yoisho-assets' do
  tag 'latest'
  action :pull
  notifies :redeploy, 'docker_container[yoishoassets]'
end

docker_container 'yoishoassets' do
  repo 'u1ih/yoisho-assets'
  tag 'latest'
  port "#{node["yoisho"]["assets_port"]}:80"
end

# Stock Quote API
docker_image 'u1ih/yoisho-stockquote' do
  tag 'latest'
  action :pull
  notifies :redeploy, 'docker_container[yoishostockquote]'
end

docker_container 'yoishostockquote' do
  repo 'u1ih/yoisho-stockquote'
  tag 'latest'
  port "#{node["yoisho"]["stockquote_port"]}:8080"
end

# Fixed Deposit API
docker_image 'u1ih/yoisho-deposit' do
  tag 'latest'
  action :pull
  notifies :redeploy, 'docker_container[yoishodeposit]'
end

docker_container 'yoishodeposit' do
  repo 'u1ih/yoisho-deposit'
  tag 'latest'
  port "#{node["yoisho"]["deposit_port"]}:8080"
end

# Account API and OAuth Service
docker_image 'u1ih/yoisho-account' do
  tag 'latest'
  action :pull
  notifies :redeploy, 'docker_container[yoishoaccount]'
end

docker_container 'yoishoaccount' do
  repo 'u1ih/yoisho-account'
  tag 'latest'
  port "#{node["yoisho"]["account_port"]}:8080"
end

# Apache for hosting our landing page
package 'apache2'

service 'apache2' do
  supports status: true
  action [:enable, :start]
end

template '/var/www/html/index.html' do
  source 'index.html.erb'
  variables({ :currency_port => node['yoisho']['currency_port'], :assets_port => node['yoisho']['assets_port'], :deposit_port => node['yoisho']['deposit_port'], :stockquote_port => node['yoisho']['stockquote_port'], :account_port => node['yoisho']['account_port'], :ec2publicip => node['ec2publicip'] })
end

