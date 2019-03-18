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

    rec1 = {"lat": "35.6284713", "lon": "139.736571", "location": "Shinagawa Station"}
    rec2 = {"lat": "35.6684231", "lon": "139.6833085", "location": "Ebisu Station"}

    with io.open(db + "/1", 'w', encoding="utf-8") as outfile:
        outfile.write(unicode(json.dumps(rec1, ensure_ascii=False)))
    outfile.close()

    with io.open(db + "/2", 'w', encoding="utf-8") as outfile:
        outfile.write(unicode(json.dumps(rec2, ensure_ascii=False)))
    outfile.close()

@app.error(404)
def error404(error):
    return "Nothing here, sorry :("

@app.route("/")
def get_home():
    return dict({"info" : "Banking ATM API. Swagger at /banking/v1/swagger and /banking/v2/swagger"})

# READ
@app.route('/banking/v1/atm/<id:int>', method='GET')
@app.route('/banking/v2/atm/<id:int>', method='GET')
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
@app.route('/banking/v1/atm', method='POST')
@app.route('/banking/v2/atm', method='POST')
def create_atm():

    new_id = str(randint(100,999))
    stuff=json.load(request.body)

    with io.open(db + "/" + new_id, 'w', encoding="utf-8") as outfile:
        outfile.write(unicode(json.dumps(stuff, ensure_ascii=False)))
    outfile.close()

    response.status = 201
    return dict({"message":"created", "id": new_id})

# UPDATE
@app.route('/banking/v1/atm/<id:int>', method='PUT')
@app.route('/banking/v2/atm/<id:int>', method='PUT')
def create_atm(id):

    stuff=json.load(request.body)

    with io.open(db + "/" + str(id), 'w', encoding="utf-8") as outfile:
        outfile.write(unicode(json.dumps(stuff, ensure_ascii=False)))
    outfile.close()

    response.status = 200
    return dict({"message":"updated", "id": id})

# LIST
@app.get('/banking/v2/atm')
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

# DELETE
@app.route('/banking/v2/atm/<id:int>', method='DELETE')
def del_atm(id):
    try:
        remove(db + "/" + str(id))
        response.status = 200

        return dict({"message":"" + str(id) + " deleted"})

    except:
        response.status = 404
        return dict({"message":"ID not found"})

@app.get('/banking/v1/swagger')
def swagger():

	swagger = '''{
    "swagger": "2.0",
    "info": {
        "version": "",
        "title": "ATM Locations",
        "description": "List of ATM  locations for Yoisho Banking Corporation"
    },
    "basePath": "/banking/v1",
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
        },
        "/atm": {
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

@app.get('/banking/v2/swagger')
def swagger2():

	swagger = '''{
    "swagger": "2.0",
    "info": {
        "version": "",
        "title": "ATM Locations",
        "description": "List of ATM  locations for Yoisho Banking Corporation"
    },
    "basePath": "/banking/v2",
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
