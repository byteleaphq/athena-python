## SDK Installation

```bash
pip install git+https://github.com/byteleaphq/athena-python.git
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


res = s.brain.create_new_brain(request=operations.CreateNewBrainRequestBody(
    name='Test - brain',
))

if res.brain is not None:
    # handle response
    pass

```

<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->

## Available Resources and Operations

### [brain](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/brain/README.md)

- [create_new_brain](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/brain/README.md#create_new_brain) - Create Brain
- [get_all_brains](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/brain/README.md#get_all_brains) - Get All Brains
- [update_brain](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/brain/README.md#update_brain) - Update Brain
- [get_brain_by_id](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/brain/README.md#get_brain_by_id) - Get Brain by ID
- [delete_brain](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/brain/README.md#delete_brain) - Delete Brain

### [document](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/document/README.md)

- [create_text_document](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/document/README.md#create_text_document) - Create Text Document
- [create_url_document](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/document/README.md#create_url_document) - Create Document by URL
- [download_document](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/document/README.md#download_document) - Download
- [get_all_documents](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/document/README.md#get_all_documents) - List Documents
- [get_document_by_id](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/document/README.md#get_document_by_id) - Get Document
- [delete_document](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/document/README.md#delete_document) - Delete Document
- [upload_document](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/document/README.md#upload_document) - Upload Document
- [search_documents](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/document/README.md#search_documents) - Search documents
- [create_document_review](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/document/README.md#create_document_review) - Create document review
- [list_document_reviews](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/document/README.md#list_document_reviews) - List document reviews

### [chat](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/chat/README.md)

- [create_new_chat](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/chat/README.md#create_new_chat) - Create New Chat
- [list_chats](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/chat/README.md#list_chats) - List Chats
- [get_chat_by_id](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/chat/README.md#get_chat_by_id) - Get Chat
- [update_chat](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/chat/README.md#update_chat) - Update Chat
- [delete_chat](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/chat/README.md#delete_chat) - Delete Chat
- [create_new_chat_with_msg](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/chat/README.md#create_new_chat_with_msg) - Create New Chat With Message
- [get_response](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/chat/README.md#get_response) - Get Response
- [list_interactions](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/chat/README.md#list_interactions) - List Interactions

### [chatbot](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/chatbot/README.md)

- [post_chatbot_create](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/chatbot/README.md#post_chatbot_create) - Create Chatbot
- [get_chatbot_list](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/chatbot/README.md#get_chatbot_list) - List Chatbots
- [post_chatbot_get](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/chatbot/README.md#post_chatbot_get) - Get Chatbot
- [get_chatbot_analytics](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/chatbot/README.md#get_chatbot_analytics) - Get Chatbot analytics
- [get_chatbot_get_messages](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/chatbot/README.md#get_chatbot_get_messages) - Get Chatbot messages
- [post_chatbot_update](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/chatbot/README.md#post_chatbot_update) - Update Chatbot
- [post_chatbot_delete](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/chatbot/README.md#post_chatbot_delete) - Delete Chatbot
- [post_chatbot_reset](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/chatbot/README.md#post_chatbot_reset) - Reset Token

### [integration](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/integration/README.md)

- [post*integration_integration_name_connect*](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/integration/README.md#post_integration_integration_name_connect_) - Connect
- [post*integration_integration_name_disconnect*](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/integration/README.md#post_integration_integration_name_disconnect_) - Disconnect
- [get_integration_integration_name_list](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/integration/README.md#get_integration_integration_name_list) - List
- [post_integration_integration_name_add](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/integration/README.md#post_integration_integration_name_add) - Add To Brain

### [ogranisation](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/ogranisation/README.md)

- [get*organisation*](https://github.com/byteleaphq/athena-python/blob/main/docs/sdks/ogranisation/README.md#get_organisation_) - get user org
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->

## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an error. If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object                           | Status Code | Content Type     |
| -------------------------------------- | ----------- | ---------------- |
| errors.CreateNewBrainResponseBody      | 401         | application/json |
| errors.CreateNewBrainBrainResponseBody | 500         | application/json |
| errors.SDKError                        | 4xx-5xx     | _/_              |

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
    res = s.brain.create_new_brain(request=operations.CreateNewBrainRequestBody(
    name='Test - brain',
))

except errors.CreateNewBrainResponseBody as e:
    # handle exception
    raise(e)
except errors.CreateNewBrainBrainResponseBody as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.brain is not None:
    # handle response
    pass

```

<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->

## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| #   | Server                             | Variables |
| --- | ---------------------------------- | --------- |
| 0   | `https://backend.athenacopilot.ai` | None      |

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


res = s.brain.create_new_brain(request=operations.CreateNewBrainRequestBody(
    name='Test - brain',
))

if res.brain is not None:
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


res = s.brain.create_new_brain(request=operations.CreateNewBrainRequestBody(
    name='Test - brain',
))

if res.brain is not None:
    # handle response
    pass

```

<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->

## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library. In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

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

| Name       | Type | Scheme     |
| ---------- | ---- | ---------- |
| `password` | http | HTTP Basic |

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


res = s.brain.create_new_brain(request=operations.CreateNewBrainRequestBody(
    name='Test - brain',
))

if res.brain is not None:
    # handle response
    pass

```

<!-- End Authentication [security] -->

<!-- Start SDK Installation [installation] -->

## SDK Installation

```bash
pip install git+<UNSET>.git
```

<!-- End SDK Installation [installation] -->

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
