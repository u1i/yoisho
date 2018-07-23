from bottle import Bottle, request, response
import json
app = Bottle()

@app.get('/calculate')
@app.get('/fixeddeposit/calculate')
def depositcalc():
    deposit = int(request.query['amount'])
    years = int(request.query['years'])

    rate = 0.0315
    msg=""

    msg = "Current interest rate is " + str(rate*100) + "% pa."

    if deposit > 100000:
        response.status = 400
        response.content_type = "application/json"
        return '{"info":"Fixed deposits are only available for amounts up to 100k USD."}'

    if years > 20:
        response.status = 400
        response.content_type = "application/json"
        return '{"info":"Fixed deposits can run only for a maximum of up to 20 years."}'

    robj={}
    robj["deposit_amount"] = '{:0,.2f}'.format(deposit)
    robj["info"] = str(msg)
    robj["years"] = str(years)

    yal=[]
    for year in range(years):
        amount = deposit * (1.0 + rate) ** year
        yao = {}
        yao["year"] = str(year+1)
        yao["amount"] = '{:0,.2f}'.format(amount)
        yal.append(yao)

    robj["yield_amount"] = '{:0,.2f}'.format(amount)
    robj["yield_breakdown_by_year"] = yal

    return dict(robj)

@app.get('/swagger')
def swagger():

	swagger = '''{
	  "swagger" : "2.0",
	  "host" : "",
	  "basePath" : "/fixeddeposit",
	  "schemes" : [ "http" ],
	  "paths" : {
	    "/calculate" : {
	      "get" : {
	        "description" : "Calculates the total interest earned from a fixed deposit, along with a breakdown for the number of years the deposit is running.",
	        "operationId" : "calculate",
	        "produces" : [ "application/json" ],
	        "parameters" : [ {
	          "description" : "The number of years the fixed deposit is running.",
	          "required" : true,
	          "in" : "query",
	          "name" : "years",
	          "type" : "string"
	        }, {
	          "description" : "The amount for the fixed deposit",
	          "required" : true,
	          "in" : "query",
	          "name" : "amount",
	          "type" : "string"
	        } ],
	        "responses" : {
	          "200" : {
	            "description" : "OK"
	          },
	          "400" : {
	            "description" : "Invalid request"
	          }
	        }
	      }
	    }
	  },
	  "info" : {
	    "title" : "Fixed Deposit Calculator",
	    "description" : "",
	    "version" : "1.0"
	  }
	}'''

	return swagger
