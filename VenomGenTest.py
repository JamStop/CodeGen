'''
Used for testing of CodeGenV1.py
'''

import json

if __name__ == "__main__":
    test_route1 = '''
    {
        "path": "/users/:id",
        "method": "GET",
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
                        "required": false
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
    }
    '''

    parsed_route1 = json.loads(test_route1)
    print(parsed_route1)
