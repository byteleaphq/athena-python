# athena-copilot-sdk

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/advanced-setup/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+<UNSET>.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import athenacopilotsdk
from athenacopilotsdk.models import components, operations

s = athenacopilotsdk.AthenaCopilotSDK(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
        password="<YOUR_PASSWORD_HERE>",
    ),
)

res = s.brain.post_brain_(request=operations.PostBrainRequestBody(
    name='Test - brain',
))

if res.object is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [brain](docs/sdks/brain/README.md)

* [post_brain_](docs/sdks/brain/README.md#post_brain_) - Create Brain
* [get_brain_](docs/sdks/brain/README.md#get_brain_) - Get All Brains
* [put_brain_brain_id_](docs/sdks/brain/README.md#put_brain_brain_id_) - Update Brain
* [get_brain_brain_id_](docs/sdks/brain/README.md#get_brain_brain_id_) - Get Brain by ID
* [delete_brain_brain_id_](docs/sdks/brain/README.md#delete_brain_brain_id_) - Delete Brain

### [document](docs/sdks/document/README.md)

* [post_document_brain_id_text](docs/sdks/document/README.md#post_document_brain_id_text) - Create Text Document
* [post_document_brain_id_url](docs/sdks/document/README.md#post_document_brain_id_url) - Create Document by URL
* [get_document_brain_id_document_id_download](docs/sdks/document/README.md#get_document_brain_id_document_id_download) - Download
* [get_document_brain_id_](docs/sdks/document/README.md#get_document_brain_id_) - List Documents
* [get_document_brain_id_document_id_](docs/sdks/document/README.md#get_document_brain_id_document_id_) - Get Document
* [delete_document_brain_id_document_id_](docs/sdks/document/README.md#delete_document_brain_id_document_id_) - Delete Document
* [post_document_brain_id_file](docs/sdks/document/README.md#post_document_brain_id_file) - Upload Document

### [chat](docs/sdks/chat/README.md)

* [post_chat_](docs/sdks/chat/README.md#post_chat_) - Create New Chat
* [get_chat_](docs/sdks/chat/README.md#get_chat_) - List Chats
* [get_chat_chat_id_](docs/sdks/chat/README.md#get_chat_chat_id_) - Get Chat
* [put_chat_chat_id_](docs/sdks/chat/README.md#put_chat_chat_id_) - Update Chat
* [delete_chat_chat_id_](docs/sdks/chat/README.md#delete_chat_chat_id_) - Delete Chat
* [post_chat_get_response](docs/sdks/chat/README.md#post_chat_get_response) - Get Response
* [post_chat_list_interactions](docs/sdks/chat/README.md#post_chat_list_interactions) - List Interactions

### [chatbot](docs/sdks/chatbot/README.md)

* [post_chatbot_create](docs/sdks/chatbot/README.md#post_chatbot_create) - Create Chatbot
* [post_chatbot_list](docs/sdks/chatbot/README.md#post_chatbot_list) - List Chatbots
* [post_chatbot_get](docs/sdks/chatbot/README.md#post_chatbot_get) - Get Chatbot
* [get_chatbot_analytics](docs/sdks/chatbot/README.md#get_chatbot_analytics) - Get Chatbot analytics
* [get_chatbot_get_messages](docs/sdks/chatbot/README.md#get_chatbot_get_messages) - Get Chatbot messages
* [post_chatbot_update](docs/sdks/chatbot/README.md#post_chatbot_update) - Update Chatbot
* [post_chatbot_delete](docs/sdks/chatbot/README.md#post_chatbot_delete) - Delete Chatbot
* [post_chatbot_reset](docs/sdks/chatbot/README.md#post_chatbot_reset) - Reset Token

### [integration](docs/sdks/integration/README.md)

* [get_integration_integration_name_connect](docs/sdks/integration/README.md#get_integration_integration_name_connect) - Connect
* [get_integration_integration_name_disconnect](docs/sdks/integration/README.md#get_integration_integration_name_disconnect) - Disconnect
* [get_integration_integration_name_list](docs/sdks/integration/README.md#get_integration_integration_name_list) - List
* [post_integration_integration_name_add](docs/sdks/integration/README.md#post_integration_integration_name_add) - Add To Brain

### [ogranisation](docs/sdks/ogranisation/README.md)

* [get_organisation_](docs/sdks/ogranisation/README.md#get_organisation_) - get user org
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object                      | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PostBrainResponseBody      | 401                               | application/json                  |
| errors.PostBrainBrainResponseBody | 500                               | application/json                  |
| errors.SDKError                   | 4xx-5xx                           | */*                               |

### Example

```python
import athenacopilotsdk
from athenacopilotsdk.models import components, errors, operations

s = athenacopilotsdk.AthenaCopilotSDK(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
        password="<YOUR_PASSWORD_HERE>",
    ),
)

res = None
try:
    res = s.brain.post_brain_(request=operations.PostBrainRequestBody(
    name='Test - brain',
))
except errors.PostBrainResponseBody as e:
    # handle exception
    raise(e)
except errors.PostBrainBrainResponseBody as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.object is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://backend.athenacopilot.ai` | None |

#### Example

```python
import athenacopilotsdk
from athenacopilotsdk.models import components, operations

s = athenacopilotsdk.AthenaCopilotSDK(
    server_idx=0,
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
        password="<YOUR_PASSWORD_HERE>",
    ),
)

res = s.brain.post_brain_(request=operations.PostBrainRequestBody(
    name='Test - brain',
))

if res.object is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import athenacopilotsdk
from athenacopilotsdk.models import components, operations

s = athenacopilotsdk.AthenaCopilotSDK(
    server_url="https://backend.athenacopilot.ai",
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
        password="<YOUR_PASSWORD_HERE>",
    ),
)

res = s.brain.post_brain_(request=operations.PostBrainRequestBody(
    name='Test - brain',
))

if res.object is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import athenacopilotsdk
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = athenacopilotsdk.AthenaCopilotSDK(client=http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name       | Type       | Scheme     |
| ---------- | ---------- | ---------- |
| `password` | http       | HTTP Basic |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. For example:
```python
import athenacopilotsdk
from athenacopilotsdk.models import components, operations

s = athenacopilotsdk.AthenaCopilotSDK(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
        password="<YOUR_PASSWORD_HERE>",
    ),
)

res = s.brain.post_brain_(request=operations.PostBrainRequestBody(
    name='Test - brain',
))

if res.object is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
