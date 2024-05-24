# Chat
(*chat*)

### Available Operations

* [post_chat_](#post_chat_) - Create New Chat
* [get_chat_](#get_chat_) - List Chats
* [get_chat_chat_id_](#get_chat_chat_id_) - Get Chat
* [put_chat_chat_id_](#put_chat_chat_id_) - Update Chat
* [delete_chat_chat_id_](#delete_chat_chat_id_) - Delete Chat
* [post_chat_get_response](#post_chat_get_response) - Get Response
* [post_chat_list_interactions](#post_chat_list_interactions) - List Interactions

## post_chat_

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


res = s.chat.post_chat_(request=operations.PostChatRequestBody(
    brain_id='{{brain_id}}',
    name='Test_chat2',
    integration=operations.Integration.FILES,
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.PostChatRequestBody](../../models/operations/postchatrequestbody.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.PostChatResponse](../../models/operations/postchatresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_chat_

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


res = s.chat.get_chat_()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetChatResponse](../../models/operations/getchatresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_chat_chat_id_

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


res = s.chat.get_chat_chat_id_(chat_id='{{chat_id}}')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `chat_id`          | *str*              | :heavy_check_mark: | N/A                | {{chat_id}}        |


### Response

**[operations.GetChatChatIDResponse](../../models/operations/getchatchatidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## put_chat_chat_id_

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


res = s.chat.put_chat_chat_id_(chat_id='{{chat_id}}', request_body=operations.PutChatChatIDRequestBody(
    temperature=None,
    name='Test_chat2',
    system_message='test system message',
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          | Example                                                                                              |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `chat_id`                                                                                            | *str*                                                                                                | :heavy_check_mark:                                                                                   | N/A                                                                                                  | {{chat_id}}                                                                                          |
| `request_body`                                                                                       | [Optional[operations.PutChatChatIDRequestBody]](../../models/operations/putchatchatidrequestbody.md) | :heavy_minus_sign:                                                                                   | N/A                                                                                                  | {<br/>"temperature": null,<br/>"system_message": "test system message"<br/>}                         |


### Response

**[operations.PutChatChatIDResponse](../../models/operations/putchatchatidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_chat_chat_id_

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


res = s.chat.delete_chat_chat_id_(chat_id='8474f310-a2a9-4cf8-b16f-8d01a5a6b5fa')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `chat_id`                            | *str*                                | :heavy_check_mark:                   | N/A                                  | 8474f310-a2a9-4cf8-b16f-8d01a5a6b5fa |


### Response

**[operations.DeleteChatChatIDResponse](../../models/operations/deletechatchatidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## post_chat_get_response

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


res = s.chat.post_chat_get_response(request=operations.PostChatGetResponseRequestBody(
    chat_thread_id='d504386d-6cba-4e38-96f0-aa16b83e1cd8',
    text='hi',
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.PostChatGetResponseRequestBody](../../models/operations/postchatgetresponserequestbody.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.PostChatGetResponseResponse](../../models/operations/postchatgetresponseresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## post_chat_list_interactions

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


res = s.chat.post_chat_list_interactions(request=operations.PostChatListInteractionsRequestBody(
    chat_thread_id='d504386d-6cba-4e38-96f0-aa16b83e1cd8',
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.PostChatListInteractionsRequestBody](../../models/operations/postchatlistinteractionsrequestbody.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PostChatListInteractionsResponse](../../models/operations/postchatlistinteractionsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
