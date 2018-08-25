from bottle import Bottle, request, response, route
import json
from random import randint
from datetime import datetime
from os import walk, path, makedirs, remove
import io

app = Bottle()

#db="/dev/shm/db"
db="/tmp/db"

if not path.exists(db):
    makedirs(db)


@app.error(404)
def error404(error):
    return "Nothing here, sorry :("

# READ
@app.route('/api/atm/<id:int>', method='GET')
def get_atm(id):

    try:
        with io.open(db + "/" + str(id), mode='r', encoding='utf-8') as file_handle:
            file_content = file_handle.read()
        file_handle.close()
    except:
        response.status = 404
        return dict({"message":"ID not found"})

    this_atm=json.loads(file_content)

    return dict(this_atm)

# CREATE
@app.route('/api/atm', method='POST')
def create_atm():

    new_id = str(randint(100,999))
    stuff=json.load(request.body)

    with io.open(db + "/" + new_id, 'w', encoding="utf-8") as outfile:
        outfile.write(unicode(json.dumps(stuff, ensure_ascii=False)))

    response.status = 201
    return dict({"message":"created", "id": new_id})

# UPDATE
@app.route('/api/atm/<id:int>', method='PUT')
def create_atm(id):

    stuff=json.load(request.body)

    with io.open(db + "/" + str(id), 'w', encoding="utf-8") as outfile:
        outfile.write(unicode(json.dumps(stuff, ensure_ascii=False)))

    response.status = 204
    return dict({"message":"updated", "id": id})


# List all
@app.get('/api/atm')
def get_all_atm():

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

        this_atm=json.loads(file_content)
        this_atm["id"] = loc

        locs_list.append(this_atm)

    locs = {"result": locs_list}
    return dict(locs)

@app.route('/api/atm/<id:int>', method='DELETE')
def del_atm(id):
    try:
        remove(db + "/" + str(id))
        response.status = 204

        return dict({"message":" " + str(id) + " deleted"})

    except:
        response.status = 404
        return dict({"message":"ID not found"})


@app.get('/swagger')
def swagger():

	swagger = '''{
    "swagger": "2.0",
    "info": {
        "version": "",
        "title": "ATM Locations",
        "description": "List of ATM  locations for Yoisho Banking Corporation"
    },
    "basePath": "/api",
    "consumes": [
        "application/json"
    ],
    "produces": [
        "application/json"
    ],
    "paths": {
        "/atm/{id}": {
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
                            "$ref": "#/definitions/api-location-input"
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
                            "$ref": "#/definitions/api-location-input"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/api-location-input"
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
        "/atm": {
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
                                        "lat": "35.6684231",
                                        "lon": "139.6833085",
                                        "location": "Ebisu Station"
                                    },
                                    {
                                        "lat": "35.6284713",
                                        "lon": "139.736571",
                                        "location": "Shinagawa Station"
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
                            "$ref": "#/definitions/api-location-input"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "",
                        "schema": {
                            "$ref": "#/definitions/api-location-input"
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
