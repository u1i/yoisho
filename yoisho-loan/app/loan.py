from bottle import Bottle, request, response, route
import json
from random import randint
from datetime import datetime
from os import walk, path, makedirs, remove
import io

app = Bottle()

# Find out whether we can use the ram disk, otherwise /tmp
if path.exists("/dev/shm"):
    db="/dev/shm/db"
else:
    db="/tmp/db"

# Initialize database
if not path.exists(db):
    makedirs(db)

    rec1 = {"name": "Zero Interest Loan 12 Months", "interest_rate": "0","fee": "2%"}
    rec2 = {"name": "Smart Loan 6 Months", "interest_rate": "1","fee": "129"}

    with io.open(db + "/1", 'w', encoding="utf-8") as outfile:
        outfile.write(unicode(json.dumps(rec1, ensure_ascii=False)))
    outfile.close()

    with io.open(db + "/2", 'w', encoding="utf-8") as outfile:
        outfile.write(unicode(json.dumps(rec2, ensure_ascii=False)))
    outfile.close()

@app.error(404)
def error404(error):
    return "Nothing here, sorry :("

# READ
@app.route('/api/loanproducts/<id:int>', method='GET')
def get_card(id):

    try:
        with io.open(db + "/" + str(id), mode='r', encoding='utf-8') as file_handle:
            file_content = file_handle.read()
        file_handle.close()
    except:
        response.status = 404
        return dict({"message":"ID not found"})

    this_card=json.loads(file_content)

    return dict(this_card)

# CREATE
@app.route('/api/loanproducts', method='POST')
def create_card():

    new_id = str(randint(100,999))
    stuff=json.load(request.body)

    with io.open(db + "/" + new_id, 'w', encoding="utf-8") as outfile:
        outfile.write(unicode(json.dumps(stuff, ensure_ascii=False)))
    outfile.close()

    response.status = 201
    return dict({"message":"created", "id": new_id})

# UPDATE
@app.route('/api/loanproducts/<id:int>', method='PUT')
def create_card(id):

    stuff=json.load(request.body)

    with io.open(db + "/" + str(id), 'w', encoding="utf-8") as outfile:
        outfile.write(unicode(json.dumps(stuff, ensure_ascii=False)))
    outfile.close()

    response.status = 200
    return dict({"message":"updated", "id": id})


# LIST
@app.get('/api/loanproducts')
def get_all_card():

    f = []
    locs_list= []
    for (dirpath, dirnames, filenames) in walk(db):
        f.extend(filenames)
        break

    for loc in f:

        try:
            with io.open(db + "/" + loc, mode='r', encoding='utf-8') as file_handle:
                file_content = file_handle.read()
            file_handle.close()
        except:
            response.status = 404
            return dict({"message":"ID not found"})

        this_card=json.loads(file_content)
        this_card["id"] = loc

        locs_list.append(this_card)

    locs = {"result": locs_list}
    return dict(locs)

# DELETE
@app.route('/api/loanproducts/<id:int>', method='DELETE')
def del_card(id):
    try:
        remove(db + "/" + str(id))
        response.status = 200

        return dict({"message":"" + str(id) + " deleted"})

    except:
        response.status = 404
        return dict({"message":"ID not found"})


@app.get('/swagger')
def swagger():

	swagger = '''{
    "swagger": "2.0",
    "info": {
        "version": "",
        "title": "Loan",
        "description": "Short term loans - interest rates and admin fees."
    },
    "basePath": "/api",
    "consumes": [
        "application/json"
    ],
    "produces": [
        "application/json"
    ],
    "paths": {
        "/loanproducts/{id}": {
            "parameters": [
                {
                    "name": "id",
                    "in": "path",
                    "required": true,
                    "type": "string"
                }
            ],
            "get": {
                "operationId": "GET-loan-products",
                "summary": "Get Loan Products",
                "tags": [
                    "Loan products"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/loan-products-input"
                        }
                    }
                }
            },
            "put": {
                "operationId": "PUT-loan-products",
                "summary": "Update Loan Products",
                "tags": [
                    "Loan products"
                ],
                "parameters": [
                    {
                        "name": "body",
                        "in": "body",
                        "schema": {
                            "$ref": "#/definitions/loan-products-input",
                            "example": {
                                "name": "Zero Interest Loan",
                                "interest_rate": "0",
                                "fee": "2%"
                            }
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/loan-products-input"
                        }
                    }
                }
            },
            "delete": {
                "operationId": "DELETE-loan-products",
                "summary": "Delete Loan Products",
                "tags": [
                    "Loan products"
                ],
                "responses": {
                    "204": {
                        "description": ""
                    }
                }
            }
        },
        "/loanproducts": {
            "get": {
                "operationId": "LIST-loan-products",
                "summary": "List Loan products",
                "tags": [
                    "Loan products"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/loan-products-input"
                            }
                        }
                    }
                }
            },
            "post": {
                "operationId": "POST-loan-products",
                "summary": "Create Loan Products",
                "tags": [
                    "Loan products"
                ],
                "parameters": [
                    {
                        "name": "body",
                        "in": "body",
                        "schema": {
                            "$ref": "#/definitions/loan-products-input",
                            "example": {
                                "name": "Zero Interest Loan",
                                "interest_rate": "0",
                                "fee": "2%"
                            }
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/loan-products-input"
                        }
                    }
                }
            }
        }
    },
    "definitions": {
        "loan-products-input": {
            "title": "Loan Products Input",
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "interest_rate": {
                    "type": "string"
                },
                "fee": {
                    "type": "string"
                }
            },
            "required": [
                "name",
                "interest_rate",
                "fee"
            ],
            "example": {
                "name": "Zero Interest Loan",
                "interest_rate": "0",
                "fee": "2%"
            }
        }
    }
}'''
	return swagger
