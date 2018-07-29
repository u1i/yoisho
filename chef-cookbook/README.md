# Yoisho - Chef Cookbook

A chef cookbook that installs the API backends of the [Yoisho Project](https://github.com/u1i/yoisho/tree/master/chef-cookbook) on a Linux node.

<img src="https://raw.githubusercontent.com/u1i/yoisho/master/resources/yoisho-logo.png" width="250"/>

## The recipe does the following:

* installs Docker on the host and starts the service
* pulls the Yoisho containers for all API endpoints: currency (SOAP/REST), assets (XML/SOAP), fixed deposit (REST/JSON), stock quote (REST/JSON) and account (OAuth) and runs them
* installs Apache2 and creates a landing page to the live endpoints and API/WSDL definitions

## Tested on the following operating systems:

* Ubuntu Server 16.04 LTS (AWS AMI ami-51a7aa2d)
 
