# xero-sdk-py
Python SDK to access Xero APIs

## Requirements

1. [python 3+](https://www.python.org/downloads/)
2. [Requests](https://pypi.org/project/requests/) library

## Installation

Install Xero SDK using [pip](https://pypi.org) as follows:

```
pip install xerosdk
```

## Usage

This SDK requires OAuth2 authentication credentials such as 
**client ID**, **client secret** and **refresh token**.

1. Create a connection using the XeroSDK class.

```python
from xerosdk import XeroSDK 

connection = XeroSDK(
    base_url='<XERO_BASE_URL>',
    client_id='<YOUR CLIENT ID>',
    client_secret='<YOUR CLIENT SECRET>',
    refresh_token='<YOUR REFRESH TOKEN>'
)
```

2. Access any of the API classes

```python
"""
USAGE: <XeroSDK INSTANCE>.<API_NAME>.<API_METHOD>(<PARAMETERS>)
"""

# Get a list of all Invoices
response = connection.Invoices.get_all()

# Get an Invoice by id
response = connection.Invoices.get_by_id(<invoice_id>)
```

**NOTE**: Only Invoices, Accounts, Contacts and  Tracking Categories 
API classes are defined in this SDK.
   