# Brain
(*brain*)

### Available Operations

* [create_new_brain](#create_new_brain) - Create Brain
* [get_all_brains](#get_all_brains) - Get All Brains
* [update_brain](#update_brain) - Update Brain
* [get_brain_by_id](#get_brain_by_id) - Get Brain by ID
* [delete_brain](#delete_brain) - Delete Brain

## create_new_brain

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


res = s.brain.create_new_brain(request=operations.CreateNewBrainRequestBody(
    name='Test - brain',
))

if res.brain is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateNewBrainRequestBody](../../models/operations/createnewbrainrequestbody.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreateNewBrainResponse](../../models/operations/createnewbrainresponse.md)**
### Errors

| Error Object                           | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.CreateNewBrainResponseBody      | 401                                    | application/json                       |
| errors.CreateNewBrainBrainResponseBody | 500                                    | application/json                       |
| errors.SDKError                        | 4xx-5xx                                | */*                                    |

## get_all_brains

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


res = s.brain.get_all_brains()

if res.brains is not None:
    # handle response
    pass

```


### Response

**[operations.GetAllBrainsResponse](../../models/operations/getallbrainsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update_brain

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


res = s.brain.update_brain(brain_id='<value>', request_body=operations.UpdateBrainRequestBody(
    name='Test Updated Brain',
))

if res.brain is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      | Example                                                                                          |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `brain_id`                                                                                       | *str*                                                                                            | :heavy_check_mark:                                                                               | N/A                                                                                              |                                                                                                  |
| `request_body`                                                                                   | [Optional[operations.UpdateBrainRequestBody]](../../models/operations/updatebrainrequestbody.md) | :heavy_minus_sign:                                                                               | N/A                                                                                              | {<br/>"name": "Test Updated Brain"<br/>}                                                         |


### Response

**[operations.UpdateBrainResponse](../../models/operations/updatebrainresponse.md)**
### Errors

| Error Object                   | Status Code                    | Content Type                   |
| ------------------------------ | ------------------------------ | ------------------------------ |
| errors.UpdateBrainResponseBody | 500                            | application/json               |
| errors.SDKError                | 4xx-5xx                        | */*                            |

## get_brain_by_id

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


res = s.brain.get_brain_by_id(brain_id='{{brain_id}}')

if res.brain is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `brain_id`         | *str*              | :heavy_check_mark: | N/A                | {{brain_id}}       |


### Response

**[operations.GetBrainByIDResponse](../../models/operations/getbrainbyidresponse.md)**
### Errors

| Error Object                    | Status Code                     | Content Type                    |
| ------------------------------- | ------------------------------- | ------------------------------- |
| errors.GetBrainByIDResponseBody | 404                             | application/json                |
| errors.SDKError                 | 4xx-5xx                         | */*                             |

## delete_brain

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


res = s.brain.delete_brain(brain_id='{{brain_id}}')

if res.delete_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `brain_id`         | *str*              | :heavy_check_mark: | N/A                | {{brain_id}}       |


### Response

**[operations.DeleteBrainResponse](../../models/operations/deletebrainresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
