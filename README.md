# xero-sdk-py
Python SDK to access Xero APIs

## Requirements

1. [Python 3+](https://www.python.org/downloads/)
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

# tenant_id is required to make a call to any API
tenant_id = connection.tenants.get_all()[0]['tenantId']
connection.set_tenant_id(tenant_id)
```

2. Access any of the API classes

```python
"""
USAGE: <XeroSDK INSTANCE>.<API_NAME>.<API_METHOD>(<PARAMETERS>)
"""

# Get a list of all Invoices
response = connection.invoices.get_all()

# Get a list of all Invoices using generator
for response in invoices.list_all_generator():
   print(response)

# Get an Invoice by id
response = connection.invoices.get_by_id(<invoice_id>)
```

**NOTE**: Only Tenants, Invoices, Accounts, Contacts, Items and TrackingCategories 
API classes are defined in this SDK.

## Integration Tests

1. Install [pytest](https://pypi.org/project/pytest/) package using pip as follows:

```
pip install pytest
```

2. Create a 'test_credentials.json' file at project root directory and enter Xero OAuth2 authentication credentials of 
your Xero app.

```json
{
  "base_url": "<xero_base_url>",
  "client_id": "<client_id>",
  "client_secret": "<client_secret>",
  "refresh_token": "<refresh_token>"
}
```

3. Run integration tests as follows:

```
python -m pytest tests/integration
```
   