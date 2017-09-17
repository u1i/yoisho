<img src="https://raw.githubusercontent.com/u1i/yoisho/master/resources/yoisho-logo.png" width="250"/>


# Fictional Bank SOAP & REST Webservices / APIs

Easy to run docker images that expose endpoints you can use for demos and testing.

## Bank Assets - SOAP/XML

Run the container:

`docker run -d -p 80:80 u1ih/yoisho-assets`

Get the WSDL:

`curl http://localhost/?WSDL`

<img src="https://raw.githubusercontent.com/u1i/yoisho/master/resources/wsdl.png" width="450"/>


## Currency Exchange Rates - REST/JSON

Run the container:

`docker run -d -p 80:80 u1ih/yoisho-currency`

Get the Swagger:

`curl http://localhost/swagger`

<img src="https://raw.githubusercontent.com/u1i/yoisho/master/resources/wsdl.png" width="450"/>

Get exchange rates - USD

`curl http://localhost/get_currency?currency=USD`

{"sell": "489.185", "timestamp": "2017-09-17 02:58:40.194337", "buy": "389.105"}