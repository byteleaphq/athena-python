# Brain
(*brain*)

### Available Operations

* [post_brain_](#post_brain_) - Create Brain
* [get_brain_](#get_brain_) - Get All Brains
* [put_brain_brain_id_](#put_brain_brain_id_) - Update Brain
* [get_brain_brain_id_](#get_brain_brain_id_) - Get Brain by ID
* [delete_brain_brain_id_](#delete_brain_brain_id_) - Delete Brain

## post_brain_

Create Brain

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


res = s.brain.post_brain_(request=operations.PostBrainRequestBody(
    name='Test - brain',
))

if res.brain is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.PostBrainRequestBody](../../models/operations/postbrainrequestbody.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.PostBrainResponse](../../models/operations/postbrainresponse.md)**
### Errors

| Error Object                      | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.PostBrainResponseBody      | 401                               | application/json                  |
| errors.PostBrainBrainResponseBody | 500                               | application/json                  |
| errors.SDKError                   | 4xx-5xx                           | */*                               |

## get_brain_

Get All Brains

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


res = s.brain.get_brain_()

if res.brains is not None:
    # handle response
    pass

```


### Response

**[operations.GetBrainResponse](../../models/operations/getbrainresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## put_brain_brain_id_

Update Brain

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


res = s.brain.put_brain_brain_id_(brain_id='<value>', request_body=operations.PutBrainBrainIDRequestBody(
    name='Test Updated Brain',
))

if res.brain is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              | Example                                                                                                  |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `brain_id`                                                                                               | *str*                                                                                                    | :heavy_check_mark:                                                                                       | N/A                                                                                                      |                                                                                                          |
| `request_body`                                                                                           | [Optional[operations.PutBrainBrainIDRequestBody]](../../models/operations/putbrainbrainidrequestbody.md) | :heavy_minus_sign:                                                                                       | N/A                                                                                                      | {<br/>"name": "Test Updated Brain"<br/>}                                                                 |


### Response

**[operations.PutBrainBrainIDResponse](../../models/operations/putbrainbrainidresponse.md)**
### Errors

| Error Object                       | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.PutBrainBrainIDResponseBody | 500                                | application/json                   |
| errors.SDKError                    | 4xx-5xx                            | */*                                |

## get_brain_brain_id_

Get Brain by ID

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


res = s.brain.get_brain_brain_id_(brain_id='{{brain_id}}')

if res.brain is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `brain_id`         | *str*              | :heavy_check_mark: | N/A                | {{brain_id}}       |


### Response

**[operations.GetBrainBrainIDResponse](../../models/operations/getbrainbrainidresponse.md)**
### Errors

| Error Object                       | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.GetBrainBrainIDResponseBody | 404                                | application/json                   |
| errors.SDKError                    | 4xx-5xx                            | */*                                |

## delete_brain_brain_id_

Delete Brain

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


res = s.brain.delete_brain_brain_id_(brain_id='{{brain_id}}')

if res.delete_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `brain_id`         | *str*              | :heavy_check_mark: | N/A                | {{brain_id}}       |


### Response

**[operations.DeleteBrainBrainIDResponse](../../models/operations/deletebrainbrainidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
