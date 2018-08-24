from bottle import Bottle, request
import json
from random import randint
from datetime import datetime
from os import walk, path, makedirs

app = Bottle()

#db="/dev/shm/db"
db="/tmp/db"

if not path.exists(db):
    makedirs(db)

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

		this_atm=json.loads(file_content)

		this_atm["id"] = loc
		locs_list.append(this_atm)

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
        "iss-input": {
            "title": "ISS Input",
            "type": "object",
            "properties": {
                "message": {
                    "type": "string"
                },
                "request": {
                    "type": "object",
                    "properties": {
                        "altitude": {
                            "type": "integer"
                        },
                        "datetime": {
                            "type": "integer"
                        },
                        "latitude": {
                            "type": "number"
                        },
                        "longitude": {
                            "type": "number"
                        },
                        "passes": {
                            "type": "integer"
                        }
                    }
                },
                "response": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "duration": {
                                "type": "integer"
                            },
                            "risetime": {
                                "type": "integer"
                            }
                        }
                    }
                }
            },
            "example": {
                "message": "success",
                "request": {
                    "altitude": 100,
                    "datetime": 1503729363,
                    "latitude": 1.29027,
                    "longitude": 103.851959,
                    "passes": 5
                },
                "response": [
                    {
                        "duration": 191,
                        "risetime": 1503735367
                    },
                    {
                        "duration": 635,
                        "risetime": 1503740930
                    },
                    {
                        "duration": 181,
                        "risetime": 1503746939
                    },
                    {
                        "duration": 627,
                        "risetime": 1503782602
                    },
                    {
                        "duration": 438,
                        "risetime": 1503788476
                    }
                ]
            }
        },
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
