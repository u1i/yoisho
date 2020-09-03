# Yoisho Banking Corporation

[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/release/python-270/) [![docker pulls](https://img.shields.io/badge/dynamic/json.svg?label=Docker%20Pulls%20(Currency)&url=https%3A%2F%2Fhub.docker.com%2Fv2%2Frepositories%2Fu1ih%2Fyoisho-currency%2F&query=$.pull_count&colorB=2)](https://hub.docker.com/r/u1ih/yoisho-currency/) [![docker pulls](https://img.shields.io/badge/dynamic/json.svg?label=Docker%20Pulls%20(Assets)&url=https%3A%2F%2Fhub.docker.com%2Fv2%2Frepositories%2Fu1ih%2Fyoisho-assets%2F&query=$.pull_count&colorB=2)](https://hub.docker.com/r/u1ih/yoisho-assets/) [![docker pulls](https://img.shields.io/badge/dynamic/json.svg?label=Docker%20Pulls%20(ATM)&url=https%3A%2F%2Fhub.docker.com%2Fv2%2Frepositories%2Fu1ih%2Fyoisho-atm%2F&query=$.pull_count&colorB=2)](https://hub.docker.com/r/u1ih/yoisho-atm/) [![docker pulls](https://img.shields.io/badge/dynamic/json.svg?label=Docker%20Pulls%20(Deposit)&url=https%3A%2F%2Fhub.docker.com%2Fv2%2Frepositories%2Fu1ih%2Fyoisho-deposit%2F&query=$.pull_count&colorB=2)](https://hub.docker.com/r/u1ih/yoisho-deposit/) [![docker pulls](https://img.shields.io/badge/dynamic/json.svg?label=Docker%20Pulls%20(Creditcard)&url=https%3A%2F%2Fhub.docker.com%2Fv2%2Frepositories%2Fu1ih%2Fyoisho-creditcard%2F&query=$.pull_count&colorB=2)](https://hub.docker.com/r/u1ih/yoisho-creditcard/) [![docker pulls](https://img.shields.io/badge/dynamic/json.svg?label=Docker%20Pulls%20(StockQuote)&url=https%3A%2F%2Fhub.docker.com%2Fv2%2Frepositories%2Fu1ih%2Fyoisho-stockquote%2F&query=$.pull_count&colorB=2)](https://hub.docker.com/r/u1ih/yoisho-stockquote/) [![docker pulls](https://img.shields.io/badge/dynamic/json.svg?label=Docker%20Pulls%20(Invest)&url=https%3A%2F%2Fhub.docker.com%2Fv2%2Frepositories%2Fu1ih%2Fyoisho-invest%2F&query=$.pull_count&colorB=2)](https://hub.docker.com/r/u1ih/yoisho-invest/) [![docker pulls](https://img.shields.io/badge/dynamic/json.svg?label=Docker%20Pulls%20(Loan)&url=https%3A%2F%2Fhub.docker.com%2Fv2%2Frepositories%2Fu1ih%2Fyoisho-loan%2F&query=$.pull_count&colorB=2)](https://hub.docker.com/r/u1ih/yoisho-loan/) [![docker pulls](https://img.shields.io/badge/dynamic/json.svg?label=Docker%20Pulls%20(Account)&url=https%3A%2F%2Fhub.docker.com%2Fv2%2Frepositories%2Fu1ih%2Fyoisho-account%2F&query=$.pull_count&colorB=2)](https://hub.docker.com/r/u1ih/yoisho-account/) [![GitHub license](https://img.shields.io/github/license/u1i/bambleweeny.svg)](https://github.com/u1i/yoisho/blob/master/LICENSE) [![GitHub issues](https://img.shields.io/github/issues/u1i/yoisho.svg)](https://GitHub.com/u1i/yoisho/issues/)

Open Banking APIs that expose simplified data services with plausible & dynamic content – great for enablement, demos, and POCs. Run them in containers on your local environment or in any cloud that gives you Docker.

Some of the endpoints are available online: [Live Endpoints](http://backend.yoisho.dob.jp/) | [Developer Portal](https://developer.yoisho.dob.jp/)

Available APIs and Webservices:

* Account Info & Balance - OAuth (3-legged)
* Credit Card Balance - Full CRUDL REST interface (Create, Read, Update, Delete, List)
* Bank Assets - SOAP/XML, 2 methods
* Currency Exchange Rates - REST/JSON, 1 parameter
* Payments - (currently in development, coming soon)
* Stock Quote - REST/JSON, 0 parameters, cached output.
* Fixed Deposit Calculator - REST/JSON, 2 parameters, semantic error handling, complex output
* Investments - /v1 and /v2 endpoints with respective Swagger specs
* ATM Locator - Full CRUDL REST interface (Create, Read, Update, Delete, List)
* Short Loan Product - Full CRUDL REST interface (Create, Read, Update, Delete, List)

[![](./resources/devp1.png)](https://developer.yoisho.dob.jp/)

Looking for a quick way to deploy? [Docker Compose](docker-compose.yml) | [Chef Cookbook](chef-cookbook)

# Bank Assets - SOAP/XML

A webservice that gives you total assets and debt of the bank. Each request will produce a slightly different result - it's a busy bank so cash is flowing in & out constantly! You could use this to show SOAP to REST conversion.

### Run the container 

`docker run -d -p 8080:8080 u1ih/yoisho-assets`

### Get the WSDL

`curl http://localhost:8080/?WSDL`

<img src="https://raw.githubusercontent.com/u1i/yoisho/master/resources/wsdl.png" width="650"/>

### Import & run the request in SoapUI

<img src="https://raw.githubusercontent.com/u1i/yoisho/master/resources/soap.png" width="650"/>


# Currency Exchange Rates - REST/JSON

This API gives you exchange rates for currencies (USD, GBP and SGD) that the bank buys and sells. Each time you ask for a quote the amounts might be slighly different - they're really busy adjusting the rates constantly!

### Run the container

`docker run -d -p 8080:8080 u1ih/yoisho-currency`

### Get the Swagger

`curl http://localhost:8080/swagger`

> {"info": {"version": "1.0", "description": "", "title": "Yoisho Currency Exchange"}, "paths": {"/get_currency": {"get": {"responses": {"default": {"description": "successful operation"}}, "produces": ["application/json"], "description": "", "parameters": [{"required": true, "type": "string", "description": "The desired currency", "name": "currency", "in": "query"}], "operationId": "get_currency"}}}, "schemes": ["http"], "basePath": "/currency", "host": "", "x-axway": {"deprecated": false, "serviceType": "rest", "basePaths": [""], "corsEnabled": true, "tags": {}}, "swagger": "2.0"}

### Get exchange rates - USD (also supported: GBP, SGD)

`curl http://localhost:8080/get_currency?currency=USD`

> {"sell": "489.185", "timestamp": "2017-09-17 02:58:40.194337", "buy": "389.105"}

### Improvements - Learning Journey

When playing with the endpoint, you'll observe a couple of things:

* if you're not adding ?currency= to the request, you'll get a nasty 500 error. Of course, this should be handled by the backend properly, but it also helps highlight the contractual aspects of Swagger and the need for API Managament to only pass on API requests to the backend if it has verified its integrity
* from an API design perspective, the development team could realize that there's two things that should change: (1) we need an API base path and (2) get_currency is not exactly a good name for a resource in order to be swagger compliant and align with API design best practices

### Get the Swagger - with base path and proper resource object

`curl http://localhost:8080/fx/swagger`

### Get exchange rates (with base path)

`curl http://localhost:8080/fx/currency?currency=USD`

> {"sell": "489.185", "timestamp": "2017-09-17 02:58:40.194337", "buy": "389.105"}


# ATM Locator - REST/JSON

This API gives you a full CRUDL interface (Create, Read, Update, Delete, List) for ATM locations, using an in memory database.

Two versions:

* /banking/v1 offers CREATE, READ, UPDATE
* /banking/v2 offers CREATE, READ, UPDATE, DELETE, LIST ALL

### Run the container

`docker run -d -p 8080:8080 u1ih/yoisho-atm`

### Get the Swagger

`curl http://localhost:8080/banking/v2/swagger`

> { "swagger": "2.0", "info": { "version": "", "title": "ATM Locations", "description": "List of ATM locations for Yoisho Banking Corporation" }, "basePath": "/banking/v2", "consumes": [ "application/json" ], "produces": [ "application/json" ], "paths": { "/atm/{id}": { "parameters": [ { "name": "id", "in": "path", "required": true, "type": "string" } ], "get": { "operationId": "GET-atm-location", "summary": "Get ATM Location", "tags": [ "Atm locations" ], "responses": { "200": { "description": "", "schema": { "$ref": "#/definitions/api-location-input" } } } }, "put": { "operationId": "PUT-atm-location", "summary": "Update ATM Location", "tags": [ "Atm locations" ], "parameters": [ { "name": "body", "in": "body", "schema": { "$ref": "#/definitions/api-location-input" } } ], "responses": { "200": { "description": "", "schema": { "$ref": "#/definitions/api-location-input" } } } }, "delete": { "operationId": "DELETE-atm-location", "summary": "Delete ATM Location", "tags": [ "Atm locations" ], "responses": { "204": { "description": "" } } } }, "/atm": { "get": { "operationId": "LIST-atm-locations", "summary": "List Atm locations", "tags": [ "Atm locations" ], "responses": { "200": { "description": "", "schema": { "type": "object", "properties": { "result": { "type": "array", "items": { "type": "object", "properties": { "lat": { "type": "string" }, "lon": { "type": "string" }, "location": { "type": "string" }, "id": { "type": "string" } } } } } }, "examples": { "application/json": { "data": [ { "lat": "35.6684231", "lon": "139.6833085", "location": "Ebisu Station" }, { "lat": "35.6284713", "lon": "139.736571", "location": "Shinagawa Station" } ] } } } } }, "post": { "operationId": "POST-atm-location", "summary": "Create ATM Location", "tags": [ "Atm locations" ], "parameters": [ { "name": "body", "in": "body", "schema": { "$ref": "#/definitions/api-location-input" } } ], "responses": { "201": { "description": "", "schema": { "$ref": "#/definitions/api-location-input" } } } } } }, "definitions": { "atm-location-input": { "title": "ATM Location Input", "type": "object", "properties": { "location": { "type": "string" }, "lat": { "type": "string" }, "lon": { "type": "string" } }, "required": [ "location" ] } }

### Get an ATM Location

The entries with id 1 and 2 are prepopulated when the container starts:

`curl http://localhost:8080/banking/v2/atm/1`

> {"lat": "35.6284713", "lon": "139.736571", "location": "Shinagawa Station"}

`curl http://localhost:8080/banking/v2/atm/2`

> {"lat": "35.6684231", "lon": "139.6833085", "location": "Ebisu Station"}

### Create an ATM

`curl -X POST http://localhost:8192/banking/v2/atm -d '{ "lat": "35.4657858", "lon": "139.6201245,17", "location": "Yokohama Station" }'"`

> {"message": "created", "id": "565"}

### Delete an ATM

`curl -X DELETE http://localhost:8080/banking/v2/atm/565`

> {"message": " 565 deleted"}

### Update an ATM

`curl -X PUT http://localhost:8080/banking/v2/atm/105 -d '{"lat": "123", "lon": "982", "location": "some place"}'`

> {"message": "updated", "id": 105}

### Get all ATM's

`curl http://localhost:8080/banking/v2/atm`

> {"result": [{"lat": "35.6684231", "lon": "139.6833085", "location": "Ebisu Station", "id": "2"}, {"lat": "35.6284713", "lon": "139.736571", "location": "Shinagawa Station", "id": "1"}]}


# Credit Card Balance

This APIs works just like v2 of to the ATM locator.

### Run the container

`docker run -d -p 8080:8080 u1ih/yoisho-creditcard`

### Get the Swagger

`curl http://localhost:8080/cardservices/swagger`

# Loan Products

* [Loan Products](https://hub.docker.com/r/u1ih/yoisho-loan/)

# Investments - v1/v2

This API provides investment insights of top performing funds. One endpoint, but two different versions. Version 2 is has one additional output field (previous_performance_rating).

### Run the container

`docker run --rm -d -p 8080:8080 u1ih/yoisho-invest:latest`

### Get the Swagger (Version 1)

`curl http://localhost:8080/invest/v1/swagger`

> {"info": {"version": "", "description": "Provides investment insights of top performing funds", "title": "Investments"}, "paths": {"/investments": {"get": {"summary": "Get Top Performing Funds", "responses": {"200": {"description": "", "schema": {"$ref": "#/definitions/investments"}}}, "tags": ["Investments"], "operationId": "GET-investments"}}}, "produces": ["application/json"], "definitions": {"investments": {"items": {"type": "object", "properties": {"performance": {"type": "string"}, "currency": {"type": "string"}, "performance_rating": {"type": "string"}, "id": {"type": "string"}, "name": {"type": "string"}}}, "type": "array", "example": [{"performance": "78", "currency": "JPY", "performance_rating": "1", "id": "YB0GB893", "name": "First Arima Onsen"}, {"performance": "71", "currency": "USD", "performance_rating": "2", "id": "YB0IM691", "name": "Castle Rock Index Fund"}], "title": "investments"}}, "basePath": "/v1", "swagger": "2.0", "consumes": ["application/json"]}

### Get top performing funds (Version 1)

`curl http://localhost:8080/invest/v1/products`

> [{"performance": "78", "currency": "JPY", "performance_rating": "1", "id": "YB0GB893", "name": "First Arima Onsen"}, {"performance": "71", "currency": "USD", "performance_rating": "2", "id": "YB0IM691", "name": "Castle Rock Index Fund"}, {"performance": "69", "currency": "RMB", "performance_rating": "2", "id": "YB0SD611", "name": "Odee Hangzhou BC"}, {"performance": "56", "currency": "USD", "performance_rating": "3", "id": "YB0AA223", "name": "Sedona 500"}, {"performance": "51", "currency": "EUR", "performance_rating": "4", "id": "YB0DE781", "name": "Munich WB2"}]

### Get the Swagger (Version 2)

`curl http://localhost:8080/invest/v2/swagger`

> {"info": {"version": "", "description": "Provides investment insights of top performing funds", "title": "Investments"}, "paths": {"/investments": {"get": {"summary": "Get Top Performing Funds", "responses": {"200": {"description": "", "schema": {"$ref": "#/definitions/investments"}}}, "tags": ["Investments"], "operationId": "GET-investments"}}}, "produces": ["application/json"], "definitions": {"investments": {"items": {"type": "object", "properties": {"performance_rating": {"type": "string"}, "name": {"type": "string"}, "previous_performance_rating": {"type": "string"}, "currency": {"type": "string"}, "performance": {"type": "string"}, "id": {"type": "string"}}}, "type": "array", "example": [{"performance_rating": "1", "name": "First Arima Onsen", "previous_performance_rating": "2", "currency": "JPY", "performance": "78", "id": "YB0GB893"}, {"performance_rating": "2", "name": "Castle Rock Index Fund", "previous_performance_rating": "3", "currency": "USD", "performance": "71", "id": "YB0IM691"}], "title": "investments"}}, "basePath": "/v2", "swagger": "2.0", "consumes": ["application/json"]}

### Get top performing funds (Version 2)

`curl http://localhost:8080/invest/v2/products`

> [{"performance_rating": "1", "name": "First Arima Onsen", "previous_performance_rating": "1", "currency": "JPY", "performance": "78", "id": "YB0GB893"}, {"performance_rating": "2", "name": "Castle Rock Index Fund", "previous_performance_rating": "1", "currency": "USD", "performance": "71", "id": "YB0IM691"}, {"performance_rating": "2", "name": "Odee Hangzhou BC", "previous_performance_rating": "0", "currency": "RMB", "performance": "69", "id": "YB0SD611"}, {"performance_rating": "3", "name": "Sedona 500", "previous_performance_rating": "4", "currency": "USD", "performance": "56", "id": "YB0AA223"}, {"performance_rating": "4", "name": "Munich WB2", "previous_performance_rating": "2", "currency": "EUR", "performance": "51", "id": "YB0DE781"}]

# Stock Quote - REST/JSON

This API returns the stock price of Yoisho Banking Corp. The data updates every minute, it's also sending additional Cache-Control headers.

### Run the container

`docker run --rm -d -p 8080:8080 u1ih/yoisho-stockquote:latest`

### Get the Swagger

`curl http://localhost:8080/stockquote/swagger`

> { "swagger" : "2.0", "host" : "", "basePath" : "/stockquote", "schemes" : [ "http" ], "paths" : { "/current" : { "get" : { "description" : "", "operationId" : "get_quote", "produces" : [ "application/json" ], "responses" : { "default" : { "description" : "successful operation" } } } } }, "info" : { "title" : "Yoisho Stock Quote", "description" : "", "version" : "1.0" }, "x-axway" : { "corsEnabled" : true, "basePaths" : [ "" ], "serviceType" : "rest", "deprecated" : false, "tags" : { } } }

### Get current quote

`curl http://localhost:8080/get_quote`

> {"message": "Stock Price refreshes every minute", "stockprice": "371.44"}

# Fixed Deposit Calculator - REST/JSON

This API calculates the total interest earned from a fixed deposit, along with a breakdown for the number of years the deposit is running. Parameters: amount, number of years the fixed deposit will run

### Run the container

`docker run --rm -d -p 8080:8080 u1ih/yoisho-deposit:latest`

### Get the Swagger

`curl http://localhost:8080/swagger`

> { "swagger" : "2.0", "host" : "", "basePath" : "/fixeddeposit", "schemes" : [ "http" ], "paths" : { "/calculate" : { "get" : { "description" : "Calculates the total interest earned from a fixed deposit, along with a breakdown for the number of years the deposit is running.", "operationId" : "calculate", "produces" : [ "application/json" ], "parameters" : [ { "description" : "The number of years the fixed deposit is running.", "required" : true, "in" : "query", "name" : "years", "type" : "string" }, { "description" : "The amount for the fixed deposit", "required" : true, "in" : "query", "name" : "amount", "type" : "string" } ], "responses" : { "200" : { "description" : "OK" }, "400" : { "description" : "Invalid request" } } } } }, "info" : { "title" : "Fixed Deposit Calculator", "description" : "", "version" : "1.0" } }

### Perform Calculation

`curl "http://localhost:8080/calculate?amount=50000&years=12"`

> {"info": "Current interest rate is 3.15% pa.", "yield_breakdown_by_year": [{"amount": "50,000.00", "year": "1"}, {"amount": "51,575.00", "year": "2"}, {"amount": "53,199.61", "year": "3"}, {"amount": "54,875.40", "year": "4"}, {"amount": "56,603.98", "year": "5"}, {"amount": "58,387.00", "year": "6"}, {"amount": "60,226.19", "year": "7"}, {"amount": "62,123.32", "year": "8"}, {"amount": "64,080.20", "year": "9"}, {"amount": "66,098.73", "year": "10"}, {"amount": "68,180.84", "year": "11"}, {"amount": "70,328.53", "year": "12"}], "deposit_amount": "50,000.00", "yield_amount": "70,328.53", "years": "12"}

# Account Info & Balance - REST/JSON OAuth

Gives you an account balance API with a 3-legged OAuth flow including consumer banking login.

##### 3-legged OAuth components

1. Consumer: the app, identified by client\_id and client\_secret
2. Resource Owner: the banking customer, here it's Dave and Jane
3. API: the account balance service

![](https://raw.githubusercontent.com/u1i/yoisho/master/resources/account-2.png)

### Credentials:

* client_id: 7b6fc8ed5127b0b2f076d
* client_secret: 724e6890757b0ae624684b70e111b705fe6b050c
* user accounts: jane, dave (use any random password)

### Run the container

`docker run --rm -d -p 8080:8080 u1ih/yoisho-account:latest`

### Start the flow

Access this URL in the browser (replace the redirect_uri with your own):

`http://localhost:8080/authorize?redirect_uri=http://www3.sotong.io&client_id=7b6fc8ed5127b0b2f076d`

Login with either 'dave' or 'jane' (any random password).

> ?code=4990047

### Get the access_token - valid for 60 seconds

Use the code from the previous step to exchange it for an access token. Of course, you'd typically do that server side.

`curl http://localhost:8080/access_token?code=4990047&client_id=7b6fc8ed5127b0b2f076d&client_secret=724e6890757b0ae624684b70e111b705fe6b050c`

> {"token_type": "bearer", "scope": "read", "access_token": "eSlcNwnLxTuzsYXyzFrhGGU3mrCKPxQ5fy51Jx93.MTUzMjM1NDM0OA=="}
>

### Get account info for user

Now with this access token we can call the actual API and retrieve the account info from the resource owner, which is the banking client.

`curl -X GET http://localhost:8080/info -H 'Authorization: Bearer eSlcNwnLxTuzsYXyzFrhGGU3mrCKPxQ5fy51Jx93.MTUzMjM1NDM0OA=='`

> {"account_owner": "dave", "fullname": "Dave Thompson", "email": "daveth271@gmail.com", "address": "491-1295, Nishimiyanosawa 6-jo, Teine-ku Sapporo-shi, Hokkaido", "phone": "+8183-977-7817"}
>


### Get account balance for user

With the same access token we retrieve the account balance from the resource owner, which is the banking client.

`curl -X GET http://localhost:8080/balance -H 'Authorization: Bearer eSlcNwnLxTuzsYXyzFrhGGU3mrCKPxQ5fy51Jx93.MTUzMjM1NDM0OA=='`

> {"account_owner": "dave", "account_balance": "10,187.91"}
>

### OAuth client - Python implementation

Here's a simple web based client implementation that shows the entire flow in the browser - the banking customer logs in and authorizes the app to access the account balance on their behalf: [Yoisho OAuth Client (Python)](https://github.com/u1i/yoisho/tree/master/yoisho-account-oauth-client)


[What does yoisho mean?](https://www.japantimes.co.jp/life/2013/03/25/language/yoisho-a-word-to-move-mountains-and-smaller-things/#.W2a6mv4zbMI)
