{
    "apis": {
        "children": {
            "/ingressaclentrytemplates/{id}/jobs": {
                "RESTName": "job", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "POST"
                    }
                ], 
                "resourceName": "jobs"
            }, 
            "/ingressaclentrytemplates/{id}/statistics": {
                "RESTName": "statistics", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "statistics"
            }
        }, 
        "parents": {
            "/domains/{id}/ingressaclentrytemplates": {
                "RESTName": "domain", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "domains"
            }, 
            "/ingressaclentrytemplates": {
                "RESTName": "ingressaclentrytemplate", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "ingressaclentrytemplates"
            }, 
            "/ingressacltemplates/{id}/ingressaclentrytemplates": {
                "RESTName": "ingressacltemplate", 
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
                "resourceName": "ingressacltemplates"
            }, 
            "/l2domains/{id}/ingressaclentrytemplates": {
                "RESTName": "l2domain", 
                "operations": [
                    {
                        "availability": null, 
                        "method": "GET"
                    }
                ], 
                "resourceName": "l2domains"
            }
        }, 
        "self": {
            "/ingressaclentrytemplates/{id}": {
                "RESTName": "ingressaclentrytemplate", 
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
                "resourceName": "ingressaclentrytemplates"
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
        "RESTName": "ingressaclentrytemplate", 
        "attributes": {
            "DSCP": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "DSCP match condition to be set in the rule. It is either * or from 0-63", 
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
            "action": {
                "allowedChars": null, 
                "allowedChoices": [
                    "FORWARD", 
                    "REDIRECT", 
                    "DROP"
                ], 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The action of the ACL entry DROP or FORWARD or REDIRECT. Action REDIRECT is allowed only for IngressAdvancedForwardingEntry Possible values are DROP, FORWARD, REDIRECT, .", 
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
            "addressOverride": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Overrides the source IP macentries will use this adress as the match criteria.", 
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
            "associatedApplicationID": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The associated application ID", 
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
            "associatedApplicationObjectID": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The associated application object ID", 
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
            "associatedApplicationObjectType": {
                "allowedChars": null, 
                "allowedChoices": [
                    "FORWARD", 
                    "REDIRECT", 
                    "DROP"
                ], 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The associated application object type Refer to API section for supported types.", 
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
            "associatedLiveEntityID": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "", 
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
            "description": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Description of the ACL entry", 
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
            "destinationPort": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The destination port to be matched if protocol is UDP or TCP. Value should be either * or single port number or a port range", 
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
            "etherType": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Ether type of the packet to be matched. etherType can be * or a valid hexadecimal value", 
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
            "locationID": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The ID of the location entity (Subnet/Zone/VportTag)", 
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
            "locationType": {
                "allowedChars": null, 
                "allowedChoices": [
                    "VPORTTAG", 
                    "SUBNET", 
                    "ANY", 
                    "POLICYGROUP", 
                    "REDIRECTIONTARGET", 
                    "ZONE"
                ], 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Type of the location entity - ANY or SUBNET or ZONE or VPORTTAG Possible values are ANY, SUBNET, ZONE, POLICYGROUP, REDIRECTIONTARGET, VPORTTAG, .", 
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
            "networkID": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The destination network entity that is referenced(subnet/zone/macro)", 
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
            "networkType": {
                "allowedChars": null, 
                "allowedChoices": [
                    "SUBNET", 
                    "NETWORK_MACRO_GROUP", 
                    "ANY", 
                    "PUBLIC_NETWORK", 
                    "ENTERPRISE_NETWORK", 
                    "POLICYGROUP", 
                    "ENDPOINT_SUBNET", 
                    "ENDPOINT_DOMAIN", 
                    "ENDPOINT_ZONE", 
                    "ZONE"
                ], 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Type of the source network -  VM_SUBNET or VM_ZONE or VM_DOMAIN or SUBNET or ZONE or ENTERPRISE_NETWORK or PUBLIC_NETWORK or ANY Possible values are ENDPOINT_SUBNET, ENDPOINT_ZONE, ENDPOINT_DOMAIN, SUBNET, ZONE, ENTERPRISE_NETWORK, PUBLIC_NETWORK, POLICYGROUP, NETWORK_MACRO_GROUP, ANY, .", 
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
            "policyState": {
                "allowedChars": null, 
                "allowedChoices": [
                    "DRAFT", 
                    "LIVE"
                ], 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": " Possible values are DRAFT, LIVE, .", 
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
            "priority": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The priority of the ACL entry that determines the order of entries", 
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
            "protocol": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Protocol number that must be matched", 
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
            "reflexive": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "true means that this ACL entry is reflexive, so there will be a corresponding egress rule that will be created by OVS in the network. false means that there is no corresponding egress rule created by OVS in the network", 
                "filterable": false, 
                "format": null, 
                "maxLength": null, 
                "maxValue": null, 
                "minLength": null, 
                "minValue": null, 
                "orderable": false, 
                "readOnly": false, 
                "required": false, 
                "type": "boolean", 
                "unique": false, 
                "uniqueItems": false
            }, 
            "sourcePort": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "Source port to be matched if protocol is UDP or TCP. Value can be either * or single port number or a port range", 
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
            "statsID": {
                "allowedChars": null, 
                "allowedChoices": null, 
                "autogenerated": false, 
                "availability": null, 
                "creationOnly": false, 
                "defaultOrder": false, 
                "defaultValue": null, 
                "description": "The statsID that is created in the VSD and identifies this ACL Template Entry. This is auto-generated by VSD", 
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
        "description": "Defines the template of Ingress ACL entries", 
        "entityName": "IngressACLEntryTemplate", 
        "package": "/policy/acl", 
        "resourceName": "ingressaclentrytemplates"
    }
}