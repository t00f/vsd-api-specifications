{
    "apis": {
        "children": {
            "/addressranges/{id}/eventlogs": {
                "RESTName": "eventlog", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "eventlogs"
            }
        }, 
        "parents": {
            "/l2domains/{id}/addressranges": {
                "RESTName": "l2domain", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "l2domains"
            }, 
            "/l2domaintemplates/{id}/addressranges": {
                "RESTName": "l2domaintemplate", 
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
                "resourceName": "l2domaintemplates"
            }, 
            "/sharednetworkresources/{id}/addressranges": {
                "RESTName": "sharednetworkresource", 
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
                "resourceName": "sharednetworkresources"
            }, 
            "/subnets/{id}/addressranges": {
                "RESTName": "subnet", 
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
                "resourceName": "subnets"
            }, 
            "/subnettemplates/{id}/addressranges": {
                "RESTName": "subnettemplate", 
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
                "resourceName": "subnettemplates"
            }
        }, 
        "self": {
            "/addressranges/{id}": {
                "RESTName": "addressrange", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "PUT"
                    }, 
                    {
                        "availability": null, 
                        "method": "DELETE"
                    }, 
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "addressranges"
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
        "RESTName": "addressrange", 
        "attributes": {
            "DHCPPoolType": {
                "allowedChars": null, 
                "allowedChoices": [
                    "HOST", 
                    "BRIDGE"
                ], 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "DHCPPoolType is an enum that indicates if the DHCP Pool is for HOST/BRIDGE. Possible values are HOST, BRIDGE Possible values are HOST, BRIDGE, .", 
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
            "maxAddress": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Higest address in the address range", 
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
            "minAddress": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Lowest address in the address range", 
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
            }
        }, 
        "description": "This is the definition of a Address Range associated with a Network", 
        "entityName": "AddressRange", 
        "package": "/network", 
        "resourceName": "addressranges"
    }
}