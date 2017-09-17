<img src="https://raw.githubusercontent.com/u1i/yoisho/master/resources/yoisho-logo.png" width="250"/>

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

> {"info": {"version": "1.0", "description": "", "title": "Yoisho Currency Exchange"}, "paths": {"/get_currency": {"get": {"responses": {"default": {"description": "successful operation"}}, "produces": ["application/json"], "description": "", "parameters": [{"required": true, "type": "string", "description": "The desired currency", "name": "currency", "in": "query"}], "operationId": "get_currency"}}}, "schemes": ["http"], "basePath": "/currency", "host": "", "x-axway": {"deprecated": false, "serviceType": "rest", "basePaths": [""], "corsEnabled": true, "tags": {}}, "swagger": "2.0"}

Get exchange rates - USD (also supported: GBP, SGD)

`curl http://localhost/get_currency?currency=USD`

> {"sell": "489.185", "timestamp": "2017-09-17 02:58:40.194337", "buy": "389.105"}