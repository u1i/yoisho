# Yoisho - Chef Cookbook

A chef cookbook that gives you a machine with all API backends of the [Yoisho Project](https://github.com/u1i/yoisho/tree/master/chef-cookbook).

<img src="https://raw.githubusercontent.com/u1i/yoisho/master/resources/yoisho-logo.png" width="250"/>

## The recipe does the following:

* installs Docker on the host and starts the service
* pulls the Yoisho containers for all API endpoints: currency (SOAP/REST), assets (XML/SOAP), fixed deposit (REST/JSON), stock quote (REST/JSON) and account (OAuth) and runs them
* installs Apache2 and creates a landing page to the live endpoints and API/WSDL definitions

## How to use

### 1 - Create a Linux machine

I've tested the cookbook on an AWS machine, the script `01-create-ec2-machine-ubuntu.sh` helps you create one if you have the AWS cli set up on your workstation. Change it to use your SSH key instead and use the AMI from the AWS region of your choice.

### 2 - (Optional) Modify the port assignments

Each API & SOAP service gets a dedicated HTTP port, you can change the defaults in the cookbook: `attributes/default.rb`

### 3 - Bootstrap the machine and run the cookbook

`02-list-ec2-instances.sh` is a quick helper to list your EC2 instances, you just need to get the IP address of the Linux box for the next step. AWS Console in the browser will get you there as well.

Assuming you have your Chef server running (somewhere) and knife configured on your workstation, you can now configure the node and install everything using the cookbook:

`03-bootstrap-ubuntu-machine-with-recipe.sh <ip-address>`

> knife bootstrap $ip --ssh-user $sshuser --sudo --identity-file $ssh_key --node-name $nodename --run-list 'recipe[yoisho_backends]'

> knife node show $nodename

### 4 - Open the landing page

`http://ip-address` should now give you a landing page with links to all the endpoints, including examples and Swagger definitions and WSDL's of the SOAP services.

![](https://raw.githubusercontent.com/u1i/yoisho/master/resources/ychefpage2.png)

## Tested on the following operating systems:

* Ubuntu Server 16.04 LTS (AWS AMI ami-51a7aa2d)

## To Do

* Test & adapt for other platforms - CentOS, RHEL, SuSE
* Add a reverse proxy (e.g. with NGINX) to make the APIs accessible via virtual paths on the same standard HTTP port: `http://hostname/currency_api` instead of `http://hostname:8082/` 
