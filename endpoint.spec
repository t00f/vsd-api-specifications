{
    "attributes": {
        "description": {
            "description": "Description of the External Service.", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "name": {
            "description": "unique name of the External Service. ", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "children": {
        "eventlog": {
            "get": true, 
            "relationship": "child"
        }
    }, 
    "model": {
        "description": "Representation of End Point", 
        "entity_name": "EndPoint", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "package": "policy", 
        "resource_name": "endpoints", 
        "rest_name": "endpoint"
    }
}