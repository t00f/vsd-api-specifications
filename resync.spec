{
    "attributes": {
        "lastRequestTimestamp": {
            "description": "Time of the last timestamp received", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "lastTimeResyncInitiated": {
            "description": "Time that the resync was initiated", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "float", 
            "uniqueScope": "no"
        }, 
        "status": {
            "allowed_choices": [
                "SUCCESS", 
                "IN_PROGRESS"
            ], 
            "description": "Status of the resync - IN_PROGRESS, SUCCESS Possible values are IN_PROGRESS, SUCCESS, .", 
            "exposed": true, 
            "filterable": true, 
            "format": "free", 
            "orderable": true, 
            "type": "enum", 
            "uniqueScope": "no"
        }
    }, 
    "model": {
        "description": "Provide information about the state of a VM resync request", 
        "entity_name": "VMResync", 
        "extends": [
            "@base", 
            "@metadata"
        ], 
        "package": "vm", 
        "resource_name": "resync", 
        "rest_name": "resync"
    }
}