{
  "apis": {
    "children": {
      "/bridgeinterfaces/{id}/dhcpoptions": {
        "RESTName": "dhcpoption", 
        "entityName": "DHCPOption", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "dhcpoptions"
      }, 
      "/bridgeinterfaces/{id}/eventlogs": {
        "RESTName": "eventlog", 
        "entityName": "EventLog", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "eventlogs"
      }, 
      "/bridgeinterfaces/{id}/policydecisions": {
        "RESTName": "policydecision", 
        "entityName": "PolicyDecision", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "policydecisions"
      }, 
      "/bridgeinterfaces/{id}/policygroups": {
        "RESTName": "policygroup", 
        "entityName": "PolicyGroup", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "policygroups"
      }, 
      "/bridgeinterfaces/{id}/qos": {
        "RESTName": "qos", 
        "entityName": "QOS", 
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
        "resourceName": "qos"
      }, 
      "/bridgeinterfaces/{id}/redirectiontargets": {
        "RESTName": "redirectiontarget", 
        "entityName": "RedirectionTarget", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "redirectiontargets"
      }, 
      "/bridgeinterfaces/{id}/statistics": {
        "RESTName": "statistics", 
        "entityName": "Statistics", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "statistics"
      }, 
      "/bridgeinterfaces/{id}/tcas": {
        "RESTName": "tca", 
        "entityName": "TCA", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "tcas"
      }
    }, 
    "parents": {
      "/domains/{id}/bridgeinterfaces": {
        "RESTName": "domain", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "domains"
      }, 
      "/l2domains/{id}/bridgeinterfaces": {
        "RESTName": "l2domain", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "l2domains"
      }, 
      "/vports/{id}/bridgeinterfaces": {
        "RESTName": "vport", 
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
        "resourceName": "vports"
      }
    }, 
    "self": {
      "/bridgeinterfaces/{id}": {
        "RESTName": "bridgeinterface", 
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
        "resourceName": "bridgeinterfaces"
      }
    }
  }, 
  "model": {
    "RESTName": "bridgeinterface", 
    "attributes": {
      "VPortID": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "ID of the vport that the interface is attached to", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "VPortName": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Name of the vport that the VM is attached to", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "associatedFloatingIPAddress": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Floating Ip Address of this network interface eg: 10.1.2.1", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "attachedNetworkID": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "ID of the l2 domain or Subnet that the VM is attached to", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "attachedNetworkType": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "l2 domain or Subnet that the interface is attached to", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "ManagedObjectType", 
        "unique": false
      }, 
      "domainID": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "ID of the domain that the VM is attached to", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "domainName": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Name of the domain that the VM is attached to", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "entityScope": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Specify if scope of entity is Data center or Enterprise level", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "EntityScope", 
        "unique": false
      }, 
      "gateway": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Gateway of the subnet that the VM is connected to", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "name": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Device name associated with this interface", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "netmask": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Netmask of the subnet that the VM is attached to", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "networkName": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Name of the network that the VM is attached to", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "policyDecisionID": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "The policy decision ID for this particular  interface", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "tierID": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "ID of the tier that the interface is attached to.", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "zoneID": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "ID of the zone that the interface is attached to", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "zoneName": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Name of the zone that the VM is attached to", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }
    }, 
    "description": "Provides information for each bridge interface", 
    "entityName": "BridgeInterface", 
    "package": "/vport", 
    "resourceName": "bridgeinterfaces"
  }
}