{
    "apis": {
        "children": {}, 
        "parents": {
            "/nsgateways/{id}/bootstraps": {
                "RESTName": "nsgateway", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "nsgateways"
            }
        }, 
        "self": {
            "/bootstraps/{id}": {
                "RESTName": "bootstrap", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "PUT"
                    }, 
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "bootstraps"
            }
        }
    }, 
    "metadata": {
        "api_version": "3.2", 
        "author": "", 
        "comments": "", 
        "date": "05-19-2015", 
        "dev_backend": "", 
        "dev_frontend": "", 
        "dev_qd": "", 
        "plm": "", 
        "prd_url": "http://", 
        "revisions": []
    }, 
    "model": {
        "RESTName": "bootstrap", 
        "attributes": {
            "installerID": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The Installer ID", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "type": "string", 
                "unique": false, 
                "uniqueItems": false
            }, 
            "status": {
                "allowedChars": null, 
                "allowedChoices": [
                    "CERTIFICATE_SIGNED", 
                    "NOTIFICATION_APP_REQ_SENT", 
                    "INACTIVE", 
                    "NOTIFICATION_APP_REQ_ACK", 
                    "ACTIVE"
                ], 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Bootstrap status; can be, for example, Active, Inactive, or Notified. Possible values are INACTIVE, NOTIFICATION_APP_REQ_SENT, NOTIFICATION_APP_REQ_ACK, CERTIFICATE_SIGNED, ACTIVE, .", 
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
            }
        }, 
        "description": "Gateway bootstrap details", 
        "entityName": "Bootstrap", 
        "package": "/gateway", 
        "resourceName": "bootstraps"
    }
}