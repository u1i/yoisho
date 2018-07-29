# Yoisho - Chef Cookbook

A chef cookbook that installs the backends of the Yoisho project on a Linux node.

<img src="https://raw.githubusercontent.com/u1i/yoisho/master/resources/yoisho-logo.png" width="250"/>

The recipe does the following:

* installs Docker on the host and starts the service
* pulls the Yoisho containers for all API endpoints: currency (SOAP/REST), assets (XML/SOAP), fixed deposit (REST/JSON), stock quote (REST/JSON) and account (OAuth)
* installs Apache2 and creates a landing page to the live endpoints and API/WSDL definitions

