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

    rec1 = {"customer_name": "Peter Griffin","creditcard_number": "358160282475953","current_balance": "4300.21"}
    rec2 = {"customer_name": "Glenn Quagmire","creditcard_number": "367408446386122","current_balance": "17823.52"}

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
@app.route('/api/cards/<id:int>', method='GET')
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
@app.route('/api/cards', method='POST')
def create_card():

    new_id = str(randint(100,999))
    stuff=json.load(request.body)

    with io.open(db + "/" + new_id, 'w', encoding="utf-8") as outfile:
        outfile.write(unicode(json.dumps(stuff, ensure_ascii=False)))
    outfile.close()

    response.status = 201
    return dict({"message":"created", "id": new_id})

# UPDATE
@app.route('/api/cards/<id:int>', method='PUT')
def create_card(id):

    stuff=json.load(request.body)

    with io.open(db + "/" + str(id), 'w', encoding="utf-8") as outfile:
        outfile.write(unicode(json.dumps(stuff, ensure_ascii=False)))
    outfile.close()

    response.status = 200
    return dict({"message":"updated", "id": id})


# LIST
@app.get('/api/cards')
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
@app.route('/api/cards/<id:int>', method='DELETE')
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
        "title": "Credit Card",
        "description": "Credit card details, balance and last transactions for customers."
    },
    "basePath": "/api",
    "consumes": [
        "application/json"
    ],
    "produces": [
        "application/json"
    ],
    "paths": {
        "/cards/{id}": {
            "parameters": [
                {
                    "name": "id",
                    "in": "path",
                    "required": true,
                    "type": "string"
                }
            ],
            "get": {
                "operationId": "GET-card",
                "summary": "Get Card",
                "tags": [
                    "Cards"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/card-input"
                        }
                    }
                }
            },
            "put": {
                "operationId": "PUT-card",
                "summary": "Update Card",
                "tags": [
                    "Cards"
                ],
                "parameters": [
                    {
                        "name": "body",
                        "in": "body",
                        "schema": {
                            "$ref": "#/definitions/card-input",
                            "example": {
                                "customer_name": "Peter Griffin",
                                "creditcard_number": "4111111111111111",
                                "current_balance": "4300.21"
                            }
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/card-input"
                        }
                    }
                }
            },
            "delete": {
                "operationId": "DELETE-card",
                "summary": "Delete Card",
                "tags": [
                    "Cards"
                ],
                "responses": {
                    "204": {
                        "description": ""
                    }
                }
            }
        },
        "/cards": {
            "get": {
                "operationId": "LIST-cards",
                "summary": "List Cards",
                "tags": [
                    "Cards"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/card-input"
                            }
                        }
                    }
                }
            },
            "post": {
                "operationId": "POST-card",
                "summary": "Create Card",
                "tags": [
                    "Cards"
                ],
                "parameters": [
                    {
                        "name": "body",
                        "in": "body",
                        "schema": {
                            "$ref": "#/definitions/card-input",
                            "example": {
                                "customer_name": "Peter Griffin",
                                "creditcard_number": "4111111111111111",
                                "current_balance": "4300.21"
                            }
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/card-input"
                        }
                    }
                }
            }
        }
    },
    "definitions": {
        "card-input": {
            "title": "Card Input",
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string"
                },
                "creditcard_number": {
                    "type": "string"
                },
                "current_balance": {
                    "type": "string"
                }
            },
            "required": [
                "customer_name",
                "creditcard_number"
            ],
            "example": {
                "customer_name": "Peter Griffin",
                "creditcard_number": "4111111111111111",
                "current_balance": "4300.21"
            }
        }
    }
}'''
	return swagger
