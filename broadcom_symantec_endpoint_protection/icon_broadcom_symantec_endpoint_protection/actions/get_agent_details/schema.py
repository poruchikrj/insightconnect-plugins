# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get details about an agent by MAC address or computer hostname"


class Input:
    AGENT = "agent"
    

class Output:
    AGENT = "agent"
    

class GetAgentDetailsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent": {
      "type": "string",
      "title": "Agent",
      "description": "Agent to retrieve device from. This can be by MAC address or computer hostname",
      "order": 1
    }
  },
  "required": [
    "agent"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAgentDetailsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent": {
      "$ref": "#/definitions/agent",
      "title": "Agent",
      "description": "Agent matching the search",
      "order": 1
    }
  },
  "definitions": {
    "agent": {
      "type": "object",
      "title": "agent",
      "properties": {
        "agentId": {
          "type": "string",
          "title": "Agent ID",
          "description": "Agent ID",
          "order": 78
        },
        "agentTimeStamp": {
          "type": "integer",
          "title": "Agent Timestamp",
          "description": "Agent timestamp",
          "order": 41
        },
        "agentType": {
          "type": "string",
          "title": "Agent Type",
          "description": "Agent type",
          "order": 135
        },
        "agentUsn": {
          "type": "integer",
          "title": "Agent USN",
          "description": "Agent USN",
          "order": 64
        },
        "agentVersion": {
          "type": "string",
          "title": "Agent Version",
          "description": "Agent version",
          "order": 39
        },
        "apOnOff": {
          "type": "integer",
          "title": "AP On Off",
          "description": "AP on off",
          "order": 127
        },
        "atpDeviceId": {
          "type": "string",
          "title": "ATP Device ID",
          "description": "ATP device ID",
          "order": 6
        },
        "atpServer": {
          "type": "string",
          "title": "ATP Server",
          "description": "ATP server",
          "order": 132
        },
        "attributeExtension": {
          "type": "string",
          "title": "Attribute Extension",
          "description": "Attribute extension",
          "order": 131
        },
        "avDefsetRevision": {
          "type": "string",
          "title": "AV Definition Set Revision",
          "description": "AV definition set revision",
          "order": 49
        },
        "avDefsetSequence": {
          "type": "string",
          "title": "AV Definition Set Sequence",
          "description": "AV definition set sequence",
          "order": 93
        },
        "avDefsetVersion": {
          "type": "string",
          "title": "AV Definition Set Version",
          "description": "AV definition set version",
          "order": 75
        },
        "avEngineOnOff": {
          "type": "integer",
          "title": "AV Engine On Off",
          "description": "AV engine on off",
          "order": 4
        },
        "bashStatus": {
          "type": "integer",
          "title": "Bash status",
          "description": "Bash status",
          "order": 63
        },
        "biosVersion": {
          "type": "string",
          "title": "BIOS Version",
          "description": "BIOS version",
          "order": 97
        },
        "bwf": {
          "type": "integer",
          "title": "BWF",
          "description": "BWF",
          "order": 57
        },
        "cidsBrowserFfOnOff": {
          "type": "integer",
          "title": "CIDS Browser FF On Off",
          "description": "CIDS browser FF on off",
          "order": 79
        },
        "cidsBrowserIeOnOff": {
          "type": "integer",
          "title": "CIDS Browser IE On Off",
          "description": "CIDS browser IE on off",
          "order": 125
        },
        "cidsDefsetVersion": {
          "type": "string",
          "title": "CIDS Definition Set Version",
          "description": "CIDS definition set version",
          "order": 109
        },
        "cidsDrvMulfCode": {
          "type": "integer",
          "title": "CIDS DRV Mulf Code",
          "description": "CIDS DRV mulf code",
          "order": 96
        },
        "cidsDrvOnOff": {
          "type": "integer",
          "title": "CIDS Drv On Off",
          "description": "CIDS drv on off",
          "order": 112
        },
        "cidsEngineVersion": {
          "type": "string",
          "title": "CIDS Engine Version",
          "description": "CIDS engine version",
          "order": 73
        },
        "cidsSilentMode": {
          "type": "integer",
          "title": "CIDS Silent Mode",
          "description": "CIDS silent mode",
          "order": 100
        },
        "computerDescription": {
          "type": "string",
          "title": "Computer Description",
          "description": "Computer description",
          "order": 61
        },
        "computerName": {
          "type": "string",
          "title": "Computer Name",
          "description": "Computer name",
          "order": 113
        },
        "computerTimeStamp": {
          "type": "integer",
          "title": "Computer Timestamp",
          "description": "Computer timestamp",
          "order": 56
        },
        "computerUsn": {
          "type": "integer",
          "title": "Computer USN",
          "description": "Computer USN",
          "order": 77
        },
        "contentUpdate": {
          "type": "integer",
          "title": "Content Update",
          "description": "Content update",
          "order": 84
        },
        "creationTime": {
          "type": "integer",
          "title": "Creation Time",
          "description": "Creation time",
          "order": 101
        },
        "currentClientId": {
          "type": "string",
          "title": "Current Client ID",
          "description": "Current client ID",
          "order": 27
        },
        "daOnOff": {
          "type": "integer",
          "title": "DA On Off",
          "description": "DA on off",
          "order": 60
        },
        "deleted": {
          "type": "integer",
          "title": "Deleted",
          "description": "Deleted",
          "order": 54
        },
        "department": {
          "type": "string",
          "title": "Department",
          "description": "Department",
          "order": 119
        },
        "deploymentMessage": {
          "type": "string",
          "title": "Deployment Message",
          "description": "Deployment message",
          "order": 21
        },
        "deploymentPreVersion": {
          "type": "string",
          "title": "Deployment Pre-version",
          "description": "Deployment pre-version",
          "order": 47
        },
        "deploymentRunningVersion": {
          "type": "string",
          "title": "Deployment Running Version",
          "description": "Deployment running version",
          "order": 40
        },
        "deploymentStatus": {
          "type": "string",
          "title": "Deployment Status",
          "description": "Deployment status",
          "order": 55
        },
        "deploymentTargetVersion": {
          "type": "string",
          "title": "Deployment Target Version",
          "description": "Deployment target version",
          "order": 43
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 122
        },
        "dhcpServer": {
          "type": "string",
          "title": "DHCP Server",
          "description": "DHCP server",
          "order": 121
        },
        "diskDrive": {
          "type": "string",
          "title": "Disk Drive",
          "description": "Disk drive",
          "order": 14
        },
        "dnsServers": {
          "type": "array",
          "title": "DNS Servers",
          "description": "DNS servers",
          "items": {
            "type": "string"
          },
          "order": 51
        },
        "domainOrWorkgroup": {
          "type": "string",
          "title": "Domain or Workgroup",
          "description": "Domain or workgroup",
          "order": 80
        },
        "edrStatus": {
          "type": "integer",
          "title": "EDR Status",
          "description": "EDR status",
          "order": 12
        },
        "elamOnOff": {
          "type": "integer",
          "title": "Elam On Off",
          "description": "Elam on off",
          "order": 3
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "Email",
          "order": 29
        },
        "employeeNumber": {
          "type": "string",
          "title": "Employee Number",
          "description": "Employee number",
          "order": 23
        },
        "employeeStatus": {
          "type": "string",
          "title": "Employee Status",
          "description": "Employee status",
          "order": 67
        },
        "encryptedDevicePassword": {
          "type": "string",
          "title": "Encrypted Device Password",
          "description": "Encrypted device password",
          "order": 32
        },
        "fbwf": {
          "type": "integer",
          "title": "FBWF",
          "description": "FBWF",
          "order": 50
        },
        "firewallOnOff": {
          "type": "integer",
          "title": "Firewall On Off",
          "description": "Firewall on off",
          "order": 141
        },
        "freeDisk": {
          "type": "integer",
          "title": "Free Disk",
          "description": "Free disk",
          "order": 13
        },
        "freeMem": {
          "type": "integer",
          "title": "Free Memory",
          "description": "Free memory",
          "order": 88
        },
        "fullName": {
          "type": "string",
          "title": "Full Name",
          "description": "Full name",
          "order": 129
        },
        "gateways": {
          "type": "array",
          "title": "Gateways",
          "description": "Gateways",
          "items": {
            "type": "string"
          },
          "order": 117
        },
        "group": {
          "$ref": "#/definitions/group",
          "title": "Group",
          "description": "Group that the agent belongs to",
          "order": 1
        },
        "groupUpdateProvider": {
          "type": "boolean",
          "title": "Group Update Provider",
          "description": "Group update provider",
          "order": 11
        },
        "hardwareKey": {
          "type": "string",
          "title": "Hardware Key",
          "description": "Hardware key",
          "order": 140
        },
        "homePhone": {
          "type": "string",
          "title": "Home Phone",
          "description": "Home phone",
          "order": 59
        },
        "hypervisorVendorId": {
          "type": "string",
          "title": "Hypervisor Vendor ID",
          "description": "Hypervisor vendor ID",
          "order": 48
        },
        "idsChecksum": {
          "type": "string",
          "title": "IDS Checksum",
          "description": "IDS checksum",
          "order": 103
        },
        "idsSerialNo": {
          "type": "string",
          "title": "IDS Serial Number",
          "description": "IDS serial number",
          "order": 22
        },
        "idsVersion": {
          "type": "string",
          "title": "IDS Version",
          "description": "IDS version",
          "order": 92
        },
        "infected": {
          "type": "integer",
          "title": "Infected",
          "description": "Infected",
          "order": 86
        },
        "installType": {
          "type": "string",
          "title": "Install Type",
          "description": "Install type",
          "order": 138
        },
        "ipAddresses": {
          "type": "array",
          "title": "IP Addresses",
          "description": "IP addresses",
          "items": {
            "type": "string"
          },
          "order": 106
        },
        "isGrace": {
          "type": "integer",
          "title": "Is Grace",
          "description": "Is grace",
          "order": 76
        },
        "isNpvdiClient": {
          "type": "integer",
          "title": "Is NPVDI Client",
          "description": "Is NPVDI client",
          "order": 120
        },
        "jobTitle": {
          "type": "string",
          "title": "Job Title",
          "description": "Job title",
          "order": 18
        },
        "kernel": {
          "type": "string",
          "title": "Kernel",
          "description": "Kernel",
          "order": 34
        },
        "lastConnectedIpAddr": {
          "type": "string",
          "title": "Last Connected IP Address",
          "description": "Last connected IP address",
          "order": 38
        },
        "lastDeploymentTime": {
          "type": "integer",
          "title": "Last Deployment Time",
          "description": "Lastd eployment time",
          "order": 74
        },
        "lastDownloadTime": {
          "type": "integer",
          "title": "Last Download Time",
          "description": "Last download time",
          "order": 126
        },
        "lastHeuristicThreatTime": {
          "type": "integer",
          "title": "Last Heuristic Threat Time",
          "description": "Last heuristic threat time",
          "order": 19
        },
        "lastScanTime": {
          "type": "integer",
          "title": "Last Scan Time",
          "description": "Last scan time",
          "order": 28
        },
        "lastServerId": {
          "type": "string",
          "title": "Last server ID",
          "description": "Last server ID",
          "order": 33
        },
        "lastServerName": {
          "type": "string",
          "title": "Last Server Name",
          "description": "Last server name",
          "order": 83
        },
        "lastSiteId": {
          "type": "string",
          "title": "Last Site ID",
          "description": "Last site ID",
          "order": 25
        },
        "lastSiteName": {
          "type": "string",
          "title": "Last Site Name",
          "description": "Last site name",
          "order": 72
        },
        "lastUpdateTime": {
          "type": "integer",
          "title": "Last Update Time",
          "description": "Last update time",
          "order": 35
        },
        "lastVirusTime": {
          "type": "integer",
          "title": "Last Virus Time",
          "description": "Last virus time",
          "order": 90
        },
        "licenseExpiry": {
          "type": "integer",
          "title": "License Expiry",
          "description": "License expiry",
          "order": 115
        },
        "licenseId": {
          "type": "string",
          "title": "License Id",
          "description": "License ID",
          "order": 8
        },
        "licenseStatus": {
          "type": "integer",
          "title": "License Status",
          "description": "License status",
          "order": 9
        },
        "logicalCpus": {
          "type": "integer",
          "title": "Logical CPUs",
          "description": "Logical CPUs",
          "order": 46
        },
        "loginDomain": {
          "type": "string",
          "title": "Login Domain",
          "description": "Login domain",
          "order": 82
        },
        "logonUserName": {
          "type": "string",
          "title": "Logon Username",
          "description": "Logon username",
          "order": 114
        },
        "macAddresses": {
          "type": "array",
          "title": "MAC Addresses",
          "description": "MAC addresses",
          "items": {
            "type": "string"
          },
          "order": 102
        },
        "majorVersion": {
          "type": "integer",
          "title": "Major Version",
          "description": "Major version",
          "order": 37
        },
        "memory": {
          "type": "integer",
          "title": "Memory",
          "description": "Memory",
          "order": 87
        },
        "minorVersion": {
          "type": "integer",
          "title": "Minor Version",
          "description": "Minor version",
          "order": 71
        },
        "mobilePhone": {
          "type": "string",
          "title": "Mobile Phone",
          "description": "Mobile phone",
          "order": 17
        },
        "officePhone": {
          "type": "string",
          "title": "Office Phone",
          "description": "Office phone",
          "order": 89
        },
        "onlineStatus": {
          "type": "integer",
          "title": "Online Status",
          "description": "Online status",
          "order": 124
        },
        "operatingSystem": {
          "type": "string",
          "title": "Operating System",
          "description": "Operating system",
          "order": 104
        },
        "osBitness": {
          "type": "string",
          "title": "OS Bitness",
          "description": "OS bitness",
          "order": 108
        },
        "osElamStatus": {
          "type": "integer",
          "title": "OS ElAM Status",
          "description": "OS ELAM status",
          "order": 137
        },
        "osFlavorNumber": {
          "type": "integer",
          "title": "OS Flavor Number",
          "description": "OS flavor number",
          "order": 45
        },
        "osFunction": {
          "type": "string",
          "title": "OS Function",
          "description": "OS function",
          "order": 15
        },
        "osLanguage": {
          "type": "string",
          "title": "OS Language",
          "description": "OS language",
          "order": 116
        },
        "osMajor": {
          "type": "integer",
          "title": "OS Major Version",
          "description": "OS major version",
          "order": 42
        },
        "osMinor": {
          "type": "integer",
          "title": "OS Minor Version",
          "description": "OS minor version",
          "order": 44
        },
        "osName": {
          "type": "string",
          "title": "OS Name",
          "description": "OS name",
          "order": 65
        },
        "osServicePack": {
          "type": "string",
          "title": "OS Service Pack",
          "description": "OS service pack",
          "order": 134
        },
        "osVersion": {
          "type": "string",
          "title": "OS Version",
          "description": "OS version",
          "order": 130
        },
        "patternIdx": {
          "type": "string",
          "title": "Pattern IDX",
          "description": "Pattern IDX",
          "order": 66
        },
        "pepOnOff": {
          "type": "integer",
          "title": "PEP On Off",
          "description": "PEP on off",
          "order": 62
        },
        "physicalCpus": {
          "type": "integer",
          "title": "Physical CPUs",
          "description": "Physical CPUs",
          "order": 107
        },
        "processorClock": {
          "type": "integer",
          "title": "Processor Clock",
          "description": "Processor clock",
          "order": 16
        },
        "processorType": {
          "type": "string",
          "title": "Processor Type",
          "description": "Processor type",
          "order": 7
        },
        "profileChecksum": {
          "type": "string",
          "title": "Profile Checksum",
          "description": "Profile checksum",
          "order": 5
        },
        "profileSerialNo": {
          "type": "string",
          "title": "Profile Serial Number",
          "description": "Profile serial number",
          "order": 139
        },
        "profileVersion": {
          "type": "string",
          "title": "Profile Version",
          "description": "Profile version",
          "order": 2
        },
        "ptpOnOff": {
          "type": "integer",
          "title": "PTP On Off",
          "description": "PTP on off",
          "order": 36
        },
        "publicKey": {
          "type": "string",
          "title": "Public Key",
          "description": "Public key",
          "order": 94
        },
        "quarantineDesc": {
          "type": "string",
          "title": "Quarantine Description",
          "description": "Quarantine description",
          "order": 95
        },
        "rebootReason": {
          "type": "string",
          "title": "Reboot Reason",
          "description": "Reboot reason",
          "order": 98
        },
        "rebootRequired": {
          "type": "integer",
          "title": "Reboot Required",
          "description": "Reboot required",
          "order": 69
        },
        "securityVirtualAppliance": {
          "type": "string",
          "title": "Security Virtual Appliance",
          "description": "Security virtual appliance",
          "order": 30
        },
        "serialNumber": {
          "type": "string",
          "title": "Serial Number",
          "description": "Serial number",
          "order": 136
        },
        "snacLicenseId": {
          "type": "string",
          "title": "SNAC license ID",
          "description": "SNAC license ID",
          "order": 24
        },
        "subnetMasks": {
          "type": "array",
          "title": "Subnet Masks",
          "description": "Subnet masks",
          "items": {
            "type": "string"
          },
          "order": 70
        },
        "svaId": {
          "type": "string",
          "title": "SVA ID",
          "description": "SVA ID",
          "order": 81
        },
        "tamperOnOff": {
          "type": "integer",
          "title": "Tamper On Off",
          "description": "Tamper on off",
          "order": 133
        },
        "tdadGlobalDataDownloadTime": {
          "type": "integer",
          "title": "TDAD Global Data Download Time",
          "description": "TDAD global data download time",
          "order": 53
        },
        "tdadOnOff": {
          "type": "integer",
          "title": "TDAD On Off",
          "description": "TDAD on off",
          "order": 111
        },
        "tdadStatusId": {
          "type": "integer",
          "title": "TDAD Status ID",
          "description": "TDAD status ID",
          "order": 110
        },
        "telemetryHwid": {
          "type": "string",
          "title": "Telemetry HWID",
          "description": "Telemetry HWID",
          "order": 99
        },
        "telemetryMid": {
          "type": "string",
          "title": "Telemetry MID",
          "description": "Telemetry MID",
          "order": 91
        },
        "timeZone": {
          "type": "integer",
          "title": "Time Zone",
          "description": "Time zone",
          "order": 128
        },
        "tmpDevice": {
          "type": "string",
          "title": "Tmp Device",
          "description": "Tmp device",
          "order": 68
        },
        "totalDiskSpace": {
          "type": "integer",
          "title": "Total Disk Space",
          "description": "Total disk space",
          "order": 58
        },
        "tpmDevice": {
          "type": "string",
          "title": "TPM Device",
          "description": "TPM device",
          "order": 123
        },
        "uniqueId": {
          "type": "string",
          "title": "Unique ID",
          "description": "Unique ID",
          "order": 118
        },
        "uuid": {
          "type": "string",
          "title": "UUID",
          "description": "UUID",
          "order": 10
        },
        "uwf": {
          "type": "integer",
          "title": "UWF",
          "description": "UWF",
          "order": 26
        },
        "virtualizationPlatform": {
          "type": "string",
          "title": "Virtualization",
          "description": "Virtualization platform",
          "order": 105
        },
        "vsicStatus": {
          "type": "integer",
          "title": "VSIC Status",
          "description": "VSIC status",
          "order": 52
        },
        "winServers": {
          "type": "array",
          "title": "Winservers",
          "description": "Winservers",
          "items": {
            "type": "string"
          },
          "order": 20
        },
        "worstInfectionIdx": {
          "type": "string",
          "title": "Worst Infection IDX",
          "description": "Worst infection IDX",
          "order": 31
        },
        "writeFiltersStatus": {
          "type": "string",
          "title": "Write Filters Status",
          "description": "Write filters status",
          "order": 85
        }
      },
      "required": [
        "group"
      ],
      "definitions": {
        "domain": {
          "type": "object",
          "title": "domain",
          "properties": {
            "id": {
              "type": "string",
              "title": "ID",
              "description": "ID",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 2
            }
          }
        },
        "group": {
          "type": "object",
          "title": "group",
          "properties": {
            "domain": {
              "$ref": "#/definitions/domain",
              "title": "Domain",
              "description": "The Broadcom Symantec Endpoint Protection Manager domain to which this group belongs",
              "order": 1
            },
            "externalReferenceId": {
              "type": "string",
              "title": "External Reference ID",
              "description": "The external reference ID for this group, between 1 - 50",
              "order": 4
            },
            "fullPathName": {
              "type": "string",
              "title": "Full Path Name",
              "description": "The full path of the group including the root group, which SEPM sets. It is not user-configurable",
              "order": 3
            },
            "id": {
              "type": "string",
              "title": "ID",
              "description": "The group ID, which SEPM sets. It is not user-configurable",
              "order": 6
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "The name of the group",
              "order": 2
            },
            "source": {
              "type": "string",
              "title": "Source",
              "description": "Source",
              "order": 5
            }
          },
          "definitions": {
            "domain": {
              "type": "object",
              "title": "domain",
              "properties": {
                "id": {
                  "type": "string",
                  "title": "ID",
                  "description": "ID",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "Name",
                  "order": 2
                }
              }
            }
          }
        }
      }
    },
    "domain": {
      "type": "object",
      "title": "domain",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 2
        }
      }
    },
    "group": {
      "type": "object",
      "title": "group",
      "properties": {
        "domain": {
          "$ref": "#/definitions/domain",
          "title": "Domain",
          "description": "The Broadcom Symantec Endpoint Protection Manager domain to which this group belongs",
          "order": 1
        },
        "externalReferenceId": {
          "type": "string",
          "title": "External Reference ID",
          "description": "The external reference ID for this group, between 1 - 50",
          "order": 4
        },
        "fullPathName": {
          "type": "string",
          "title": "Full Path Name",
          "description": "The full path of the group including the root group, which SEPM sets. It is not user-configurable",
          "order": 3
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The group ID, which SEPM sets. It is not user-configurable",
          "order": 6
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the group",
          "order": 2
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "Source",
          "order": 5
        }
      },
      "definitions": {
        "domain": {
          "type": "object",
          "title": "domain",
          "properties": {
            "id": {
              "type": "string",
              "title": "ID",
              "description": "ID",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name",
              "order": 2
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)