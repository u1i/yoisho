from bottle import Bottle, request, response, route
import json
from random import randint
from datetime import datetime
from os import walk, path, makedirs, remove

app = Bottle()

#db="/dev/shm/db"
db="/tmp/db"

if not path.exists(db):
    makedirs(db)


@app.error(404)
def error404(error):
    return "Nothing here, sorry :("

# READ
@app.route('/atm/locations/<id:int>', method='GET')
def get_atm(id):

    try:
        with open(db + "/" + str(id), mode='rb') as file_handle:
            file_content = file_handle.read()
        file_handle.close()
    except:
        response.status = 404
        return dict({"message":"ID not found"})

    this_atm=json.loads(file_content)

    return dict(this_atm)

@app.route('/atm/locations/<id:int>', method='DELETE')
def del_atm(id):
    try:
        remove(db + "/" + str(id))
        return "OK" + str(id)
    except:
        response.status = 404
        return dict({"message":"ID not found"})

@app.route('/atm/locations', method='POST')
def create_atm():

    f = open(db + "/" + str(randint(100,999)), mode='w+')
    stuff=json.load(request.body)

    f.write(str(stuff))
    f.close()
    response.status = 201
    return "Created"

@app.get('/atm/locations')
def get_all_atm():

	f = []
	locs_list= []
	for (dirpath, dirnames, filenames) in walk(db):
	    f.extend(filenames)
	    break

	for loc in f:
		with open(db + "/" + loc, mode='rb') as file_handle:
			file_content = file_handle.read()
		file_handle.close()

        try:
    		this_atm=json.loads(file_content)

    		this_atm["id"] = loc
    		locs_list.append(this_atm)
        except:
            dummy=1

	locs = {"result": locs_list}
	return dict(locs)


@app.get('/swagger')
def swagger():

	swagger = '''{
    "swagger": "2.0",
    "info": {
        "version": "",
        "title": "ATM Locations",
        "description": "List of ATM  locations for Yoisho Banking Corporation"
    },
    "basePath": "/atm",
    "consumes": [
        "application/json"
    ],
    "produces": [
        "application/json"
    ],
    "paths": {
        "/locations/{id}": {
            "parameters": [
                {
                    "name": "id",
                    "in": "path",
                    "required": true,
                    "type": "string"
                }
            ],
            "get": {
                "operationId": "GET-atm-location",
                "summary": "Get ATM Location",
                "tags": [
                    "Atm locations"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/atm-location-input"
                        }
                    }
                }
            },
            "put": {
                "operationId": "PUT-atm-location",
                "summary": "Update ATM Location",
                "tags": [
                    "Atm locations"
                ],
                "parameters": [
                    {
                        "name": "body",
                        "in": "body",
                        "schema": {
                            "$ref": "#/definitions/atm-location-input"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/atm-location-input"
                        }
                    }
                }
            },
            "delete": {
                "operationId": "DELETE-atm-location",
                "summary": "Delete ATM Location",
                "tags": [
                    "Atm locations"
                ],
                "responses": {
                    "204": {
                        "description": ""
                    }
                }
            }
        },
        "/locations": {
            "get": {
                "operationId": "LIST-atm-locations",
                "summary": "List Atm locations",
                "tags": [
                    "Atm locations"
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "result": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "lat": {
                                                "type": "string"
                                            },
                                            "lon": {
                                                "type": "string"
                                            },
                                            "location": {
                                                "type": "string"
                                            },
                                            "id": {
                                                "type": "string"
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "examples": {
                            "application/json": {
                                "data": [
                                    {
                                        "lat": "111",
                                        "lon": "09393",
                                        "location": "somewhere",
                                        "id": "1"
                                    },
                                    {
                                        "lat": "22111",
                                        "lon": "209393",
                                        "location": "somewhere else",
                                        "id": "2"
                                    }
                                ]
                            }
                        }
                    }
                }
            },
            "post": {
                "operationId": "POST-atm-location",
                "summary": "Create ATM Location",
                "tags": [
                    "Atm locations"
                ],
                "parameters": [
                    {
                        "name": "body",
                        "in": "body",
                        "schema": {
                            "$ref": "#/definitions/atm-location-input"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/atm-location-input"
                        }
                    }
                }
            }
        }
    },
    "definitions": {
        "atm-location-input": {
            "title": "ATM Location Input",
            "type": "object",
            "properties": {
                "location": {
                    "type": "string"
                },
                "lat": {
                    "type": "string"
                },
                "lon": {
                    "type": "string"
                }
            },
            "required": [
                "location"
            ]
        }
    }
}'''
	return swagger
