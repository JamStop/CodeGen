'''
Used for testing of CodeGenV1.py
'''

from CodeGen import VenomGen

if __name__ == "__main__":
    metaobject = '''
    {
        "routes": {
            "filePath": "test.py",
            "ui-1234": {
                "path": "/users/:id",
                "method": "GET",
                "handler": "UserHandler",
                "handlerFile": "VenomHandlers",
                "headers": {
                    "X-Authorization": {
                        "type": "Integer",
                        "attributes": {
                            "required": false,
                            "pattern": null,
                            "min": 8
                        }
                    }
                },
                "url": {
                    "agetype": {
                        "type": "String",
                        "attributes": {
                            "required": true,
                            "pattern": null,
                            "min": null,
                            "choices": ["adult", "child"],
                            "max": null,
                            "characters": null
                        }
                    }
                },
                "query": {
                    "file": {
                        "type": "Integer",
                        "attributes": {
                            "max": null,
                            "choices": null,
                            "required": true,
                            "min": 1
                        }
                    },
                    "email": {
                        "type": "String",
                        "attributes": {
                            "max": null,
            			    "min": 5
            	        }
                    }
                },
                "body": {
                    "type": "Dict",
                    "template": {
                        "filename": {
                            "type": "String",
                            "attributes": {
                                "required": true,
                                "pattern": null,
                                "min": 3,
                                "choices": null,
                                "max": 100,
                                "characters": "abcdefghijklmnop"
                            }
                        },
                        "file": {
                            "type": "Integer",
                            "attributes": {
                                "min": 0
                            }
                        },
                        "nested": {
                            "type": "Dict",
                            "template": {
                                "foo": {
                                    "type": "Float",
                                    "attributes": {
                                        "required": true
                                    }
                                }
                            },
                            "attributes": {
                            }
                        },
                        "email": {
                            "type": "String",
                            "attributes": {
                                "min": 2,
                                "required": true,
                                "pattern": ".*"
                            }
                        }
                    }
                }
            },
            "ui-2345": {
                "path": "/users/:id1",
                "method": "GET",
                "handler": "UserHandler",
                "handlerFile": "VenomHandlers",
                "headers": {
                },
                "url": {
                },
                "query": {
                },
                "body":{
                }
            }
        }
    }
    '''

    # parsed_route1 = json.loads(test_route1)
    # parsed_route2 = json.loads(test_route2)
    # test_application = {"apps": ["test_app"]}
    #
    # vgen = CodeGenV1.VenomGen()
    # vgen.start("test")
    #
    # vgen.write_applications(test_application)
    # vgen.write_route(parsed_route1)
    # vgen.write_route(parsed_route2)
    #
    # vgen.generate("test")
    test = VenomGen.VenomGen()
    test.generate(metaobject)
