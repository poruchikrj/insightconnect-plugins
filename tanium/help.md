# Description

Testing the new format for inputs

# Key Features

Identify key features of plugin.

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product's user interface

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|domain|string|None|True|The domian of the user loggin in|None|rapid7|
|host|string|None|True|URL to service|None|https://taniumserver.rapid7.com|
|username_and_password|credential_username_password|None|True|Your username and password|None|None|
|verify_ssl|boolean|None|True|Enforce signed certificates for the tanium server|None|True|

Example input:

```
{
  "domain": "rapid7",
  "host": "https://taniumserver.rapid7.com",
  "verify_ssl": true
}
```

## Technical Details

### Actions

#### list_saved_questions

This action is used to retrieve all saved question definitions on the server..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filter|[]object|None|False|Filter results based on paramaters See tanium documentation on cache_filters for use|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|questions|[]question|True|A list of saved suestions|

Example output:

```
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### question

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Action Tracking Flag|boolean|False|Action tracking flag|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Tanium](LINK TO PRODUCT/VENDOR WEBSITE)
