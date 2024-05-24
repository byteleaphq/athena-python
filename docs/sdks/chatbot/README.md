# Chatbot
(*chatbot*)

### Available Operations

* [post_chatbot_create](#post_chatbot_create) - Create Chatbot
* [post_chatbot_list](#post_chatbot_list) - List Chatbots
* [post_chatbot_get](#post_chatbot_get) - Get Chatbot
* [get_chatbot_analytics](#get_chatbot_analytics) - Get Chatbot analytics
* [get_chatbot_get_messages](#get_chatbot_get_messages) - Get Chatbot messages
* [post_chatbot_update](#post_chatbot_update) - Update Chatbot
* [post_chatbot_delete](#post_chatbot_delete) - Delete Chatbot
* [post_chatbot_reset](#post_chatbot_reset) - Reset Token

## post_chatbot_create

Create Chatbot

### Example Usage

```python
import athenacopilotsdk
from athenacopilotsdk.models import components, operations

s = athenacopilotsdk.AthenaCopilotSDK(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.chatbot.post_chatbot_create(request=operations.PostChatbotCreateRequestBody(
    name='Chatbot -1',
    brain_id='1f1d7a6a-e45b-4974-a0ba-98935650cb9c',
    urls=[
        'https://byteleap.co',
        'https://ayushgoyal.dev',
    ],
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PostChatbotCreateRequestBody](../../models/operations/postchatbotcreaterequestbody.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.PostChatbotCreateResponse](../../models/operations/postchatbotcreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## post_chatbot_list

List Chatbots

### Example Usage

```python
import athenacopilotsdk
from athenacopilotsdk.models import components

s = athenacopilotsdk.AthenaCopilotSDK(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.chatbot.post_chatbot_list()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.PostChatbotListResponse](../../models/operations/postchatbotlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## post_chatbot_get

Get Chatbot

### Example Usage

```python
import athenacopilotsdk
from athenacopilotsdk.models import components

s = athenacopilotsdk.AthenaCopilotSDK(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.chatbot.post_chatbot_get(chatbot_id='7a2e792d-cf48-49d2-a36d-186be034a9dc')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `chatbot_id`                         | *Optional[str]*                      | :heavy_minus_sign:                   | N/A                                  | 7a2e792d-cf48-49d2-a36d-186be034a9dc |


### Response

**[operations.PostChatbotGetResponse](../../models/operations/postchatbotgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_chatbot_analytics

Get Chatbot analytics

### Example Usage

```python
import athenacopilotsdk
from athenacopilotsdk.models import components

s = athenacopilotsdk.AthenaCopilotSDK(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.chatbot.get_chatbot_analytics(chatbot_id='1a718a80-71c0-414b-915c-5c5991597ac7')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `chatbot_id`                         | *Optional[str]*                      | :heavy_minus_sign:                   | N/A                                  | 1a718a80-71c0-414b-915c-5c5991597ac7 |


### Response

**[operations.GetChatbotAnalyticsResponse](../../models/operations/getchatbotanalyticsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_chatbot_get_messages

note: there is a limit of 10000 messages

### Example Usage

```python
import athenacopilotsdk
from athenacopilotsdk.models import components

s = athenacopilotsdk.AthenaCopilotSDK(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.chatbot.get_chatbot_get_messages(chatbot_id='1a718a80-71c0-414b-915c-5c5991597ac7')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `chatbot_id`                         | *Optional[str]*                      | :heavy_minus_sign:                   | N/A                                  | 1a718a80-71c0-414b-915c-5c5991597ac7 |


### Response

**[operations.GetChatbotGetMessagesResponse](../../models/operations/getchatbotgetmessagesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## post_chatbot_update

Update Chatbot

### Example Usage

```python
import athenacopilotsdk
from athenacopilotsdk.models import components, operations

s = athenacopilotsdk.AthenaCopilotSDK(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.chatbot.post_chatbot_update(request=operations.PostChatbotUpdateRequestBody(
    name='Chatbot -1',
    urls=[
        'https://byteleap.co',
        'https://anshgoyal.com',
    ],
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.PostChatbotUpdateRequestBody](../../models/operations/postchatbotupdaterequestbody.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.PostChatbotUpdateResponse](../../models/operations/postchatbotupdateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## post_chatbot_delete

Delete Chatbot

### Example Usage

```python
import athenacopilotsdk
from athenacopilotsdk.models import components

s = athenacopilotsdk.AthenaCopilotSDK(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.chatbot.post_chatbot_delete(chatbot_id='2de69bc3-3f60-46a2-be30-e95c98ab7a87')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `chatbot_id`                         | *Optional[str]*                      | :heavy_minus_sign:                   | N/A                                  | 2de69bc3-3f60-46a2-be30-e95c98ab7a87 |


### Response

**[operations.PostChatbotDeleteResponse](../../models/operations/postchatbotdeleteresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## post_chatbot_reset

Reset Token

### Example Usage

```python
import athenacopilotsdk
from athenacopilotsdk.models import components

s = athenacopilotsdk.AthenaCopilotSDK(
    security=components.Security(
        username="<YOUR_USERNAME_HERE>",
        password="<YOUR_PASSWORD_HERE>",
    ),
)


res = s.chatbot.post_chatbot_reset(chatbot_id='c7af119a-a5c6-47a4-a5fd-fbf96ef08851')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `chatbot_id`                         | *Optional[str]*                      | :heavy_minus_sign:                   | N/A                                  | c7af119a-a5c6-47a4-a5fd-fbf96ef08851 |


### Response

**[operations.PostChatbotResetResponse](../../models/operations/postchatbotresetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
