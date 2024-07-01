# Chat
(*chat*)

### Available Operations

* [create_new_chat](#create_new_chat) - Create New Chat
* [list_chats](#list_chats) - List Chats
* [get_chat_by_id](#get_chat_by_id) - Get Chat
* [update_chat](#update_chat) - Update Chat
* [delete_chat](#delete_chat) - Delete Chat
* [create_new_chat_with_msg](#create_new_chat_with_msg) - Create New Chat With Message
* [get_response](#get_response) - Get Response
* [list_interactions](#list_interactions) - List Interactions

## create_new_chat

integration - defaults to files (superpowered). supported values - files | data-warehouse

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


res = s.chat.create_new_chat(request=operations.CreateNewChatRequestBody(
    brain_id='{{brain_id}}',
    name='Test_chat2',
    integration=operations.Integration.FILES,
))

if res.chats is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreateNewChatRequestBody](../../models/operations/createnewchatrequestbody.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreateNewChatResponse](../../models/operations/createnewchatresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_chats

List Chats

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


res = s.chat.list_chats()

if res.chats is not None:
    # handle response
    pass

```


### Response

**[operations.ListChatsResponse](../../models/operations/listchatsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_chat_by_id

Get Chat

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


res = s.chat.get_chat_by_id(chat_id='{{chat_id}}')

if res.chat is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `chat_id`          | *str*              | :heavy_check_mark: | N/A                | {{chat_id}}        |


### Response

**[operations.GetChatByIDResponse](../../models/operations/getchatbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_chat

Update Chat

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


res = s.chat.update_chat(chat_id='{{chat_id}}', request_body=operations.UpdateChatRequestBody(
    temperature=None,
    name='Test_chat2',
    system_message='test system message',
    additional_properties={

    },
))

if res.chats is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    | Example                                                                                        |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `chat_id`                                                                                      | *str*                                                                                          | :heavy_check_mark:                                                                             | N/A                                                                                            | {{chat_id}}                                                                                    |
| `request_body`                                                                                 | [Optional[operations.UpdateChatRequestBody]](../../models/operations/updatechatrequestbody.md) | :heavy_minus_sign:                                                                             | N/A                                                                                            | {<br/>"temperature": null,<br/>"system_message": "test system message"<br/>}                   |


### Response

**[operations.UpdateChatResponse](../../models/operations/updatechatresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_chat

Delete Chat

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


res = s.chat.delete_chat(chat_id='8474f310-a2a9-4cf8-b16f-8d01a5a6b5fa')

if res.chats is not None:
    # handle response
    pass

```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `chat_id`                            | *str*                                | :heavy_check_mark:                   | N/A                                  | 8474f310-a2a9-4cf8-b16f-8d01a5a6b5fa |


### Response

**[operations.DeleteChatResponse](../../models/operations/deletechatresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_new_chat_with_msg

Create a new chat with the specified brain and message.

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


res = s.chat.create_new_chat_with_msg(request=operations.CreateNewChatWithMsgRequestBody(
    brain_ids=[
        '2ad136c5-d2a2-4bbc-bc3d-974f9f88e86d',
    ],
    name='Slack Chat - 2024-06-26T12:34:56.789Z',
    message='Hello, how can I assist you today?',
))

if res.chat_interactions is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateNewChatWithMsgRequestBody](../../models/operations/createnewchatwithmsgrequestbody.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.CreateNewChatWithMsgResponse](../../models/operations/createnewchatwithmsgresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_response

Get Response

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


res = s.chat.get_response(request=operations.GetResponseRequestBody(
    chat_thread_id='d504386d-6cba-4e38-96f0-aa16b83e1cd8',
    text='hi',
))

if res.chat_interactions is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetResponseRequestBody](../../models/operations/getresponserequestbody.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetResponseResponse](../../models/operations/getresponseresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## list_interactions

List Interactions

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


res = s.chat.list_interactions(request=operations.ListInteractionsRequestBody(
    chat_thread_id='d504386d-6cba-4e38-96f0-aa16b83e1cd8',
))

if res.chat_interactions is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.ListInteractionsRequestBody](../../models/operations/listinteractionsrequestbody.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.ListInteractionsResponse](../../models/operations/listinteractionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
