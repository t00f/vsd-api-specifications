{
    "apis": {
        "children": {
            "/keyservermonitorseeds/{id}/keyservermonitorencryptedseeds": {
                "RESTName": "keyservermonitorencryptedseed", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "keyservermonitorencryptedseeds"
            }
        }, 
        "parents": {
            "/keyservermonitors/{id}/keyservermonitorseeds": {
                "RESTName": "keyservermonitor", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }, 
                    {
                        "availability": null, 
                        "method": "POST"
                    }
                ], 
                "resourceName": "keyservermonitors"
            }
        }, 
        "self": {
            "/keyservermonitorseeds/{id}": {
                "RESTName": "keyservermonitorseed", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "DELETE"
                    }, 
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "keyservermonitorseeds"
            }
        }
    }, 
    "metadata": {
        "api_version": "3.2", 
        "author": "", 
        "comments": "", 
        "date": "05-18-2015", 
        "dev_backend": "", 
        "dev_frontend": "", 
        "dev_qd": "", 
        "plm": "", 
        "prd_url": "http://", 
        "revisions": []
    }, 
    "model": {
        "RESTName": "keyservermonitorseed", 
        "attributes": {
            "creationTime": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The time this entry was created (milliseconds since epoch)", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "type": "long", 
                "unique": false, 
                "uniqueItems": false
            }, 
            "lifetime": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The lifetime of this entry (seconds)", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "type": "integer", 
                "unique": false, 
                "uniqueItems": false
            }, 
            "seedTrafficAuthenticationAlgorithm": {
                "allowedChars": null, 
                "allowedChoices": [
                    "HMAC_SHA384", 
                    "HMAC_SHA512", 
                    "HMAC_SHA1", 
                    "HMAC_MD5", 
                    "HMAC_SHA256"
                ], 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Seed traffic Authentication Algorithm. Possible values are HMAC_SHA1, HMAC_SHA256, HMAC_SHA384, HMAC_SHA512, HMAC_MD5, .", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "type": "enum", 
                "unique": false, 
                "uniqueItems": false
            }, 
            "seedTrafficEncryptionAlgorithm": {
                "allowedChars": null, 
                "allowedChoices": [
                    "Triple_DES_CBC", 
                    "AES_128_CBC", 
                    "AES_256_CBC", 
                    "AES_192_CBC"
                ], 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Seed traffic Encryption Algorithm. Possible values are AES_128_CBC, AES_192_CBC, AES_256_CBC, Triple_DES_CBC, .", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "type": "enum", 
                "unique": false, 
                "uniqueItems": false
            }, 
            "seedTrafficEncryptionKeyLifetime": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Seed Traffic Encryption Key Lifetime in Seconds", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "type": "integer", 
                "unique": false, 
                "uniqueItems": false
            }, 
            "startTime": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The time this entry  was activated (milliseconds since epoch)", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "type": "long", 
                "unique": false, 
                "uniqueItems": false
            }
        }, 
        "description": "Represents a Keyserver Monitor Seed Snapshot", 
        "entityName": "KeyServerMonitorSeed", 
        "package": "/keyserver", 
        "resourceName": "keyservermonitorseeds"
    }
}