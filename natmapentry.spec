{
    "attributes": {
        "associatedPATNATPoolID": {
            "description": "Read Only - Indicates which PATNATPool this entry belongs to", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "privateIP": {
            "description": "Private IP address of the interface", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }, 
        "publicIP": {
            "description": "Public IP address of the interface", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "required": true, 
            "type": "string", 
            "uniqueScope": "no"
        }
    }, 
    "model": {
        "delete": true, 
        "description": "Defines a MAP between the private ip and public ip", 
        "entity_name": "NATMapEntry", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "get": true, 
        "package": "gateway", 
        "resource_name": "natmapentries", 
        "rest_name": "natmapentry"
    }
}