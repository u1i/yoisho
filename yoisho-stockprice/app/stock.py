from bottle import Bottle, request, response
import json
from random import randint
from datetime import datetime

app = Bottle()

# allow both paths
@app.get('/stockquote/current')
@app.get('/get_quote')
def get_quote():

        sresp={}

	currentMinute = datetime.now().minute
	rnd = str(hash(str(currentMinute)))

	sresp['stockprice'] = "371." + rnd[-2:]
	sresp['message'] = "Stock Price refreshes every minute"

	response.headers["Cache-Control"] = "max-age=60, public"

	return dict(sresp)

@app.get('/swagger')
def swagger():

	swagger = '''{   "swagger" : "2.0",   "host" : "",   "basePath" : "/quote",   "schemes" : [ "http" ],   "paths" : {     "/get_quote" : {       "get" : {         "description" : "",         "operationId" : "get_quote",         "produces" : [ "application/json" ],           "responses" : {           "default" : {             "description" : "successful operation"           }         }       }     }   },   "info" : {     "title" : "Yoisho Stock Quote",     "description" : "",     "version" : "1.0"   },   "x-axway" : {     "corsEnabled" : true,     "basePaths" : [ "" ],     "serviceType" : "rest",     "deprecated" : false,     "tags" : { }   } }'''

	return swagger

@app.get('/stockquote/swagger')
def swagger():

	swagger = '''{   "swagger" : "2.0",   "host" : "",   "basePath" : "/stockquote",   "schemes" : [ "http" ],   "paths" : {     "/current" : {       "get" : {         "description" : "Get current stock price",         "operationId" : "get_quote",         "produces" : [ "application/json" ],           "responses" : {           "default" : {             "description" : "successful operation"           }         }       }     }   },   "info" : {     "title" : "Yoisho Stock Quote",     "description" : "",     "version" : "1.0"   },   "x-axway" : {     "corsEnabled" : true,     "basePaths" : [ "" ],     "serviceType" : "rest",     "deprecated" : false,     "tags" : { }   } }'''

	return swagger
