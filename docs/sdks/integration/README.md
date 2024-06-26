# Integration
(*integration*)

### Available Operations

* [post_integration_integration_name_connect_](#post_integration_integration_name_connect_) - Connect
* [post_integration_integration_name_disconnect_](#post_integration_integration_name_disconnect_) - Disconnect
* [get_integration_integration_name_list](#get_integration_integration_name_list) - List
* [post_integration_integration_name_add](#post_integration_integration_name_add) - Add To Brain

## post_integration_integration_name_connect_

Connect

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


res = s.integration.post_integration_integration_name_connect_(integration_name='notion')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    | Example                                                                                                        |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `integration_name`                                                                                             | *str*                                                                                                          | :heavy_check_mark:                                                                                             | Currently supported integrations are "notion" and "confluence". More integrations will be added in the future. | notion                                                                                                         |


### Response

**[operations.PostIntegrationIntegrationNameConnectResponse](../../models/operations/postintegrationintegrationnameconnectresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## post_integration_integration_name_disconnect_

Disconnect

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


res = s.integration.post_integration_integration_name_disconnect_(integration_name='notion')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    | Example                                                                                                        |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `integration_name`                                                                                             | *str*                                                                                                          | :heavy_check_mark:                                                                                             | Currently supported integrations are "notion" and "confluence". More integrations will be added in the future. | notion                                                                                                         |


### Response

**[operations.PostIntegrationIntegrationNameDisconnectResponse](../../models/operations/postintegrationintegrationnamedisconnectresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_integration_integration_name_list

list pages from integration

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


res = s.integration.get_integration_integration_name_list(integration_name='confluence')

if res.response_bodies is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    | Example                                                                                                        |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `integration_name`                                                                                             | *str*                                                                                                          | :heavy_check_mark:                                                                                             | Currently supported integrations are "notion" and "confluence". More integrations will be added in the future. | confluence                                                                                                     |


### Response

**[operations.GetIntegrationIntegrationNameListResponse](../../models/operations/getintegrationintegrationnamelistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## post_integration_integration_name_add

used to add pages to brain

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


res = s.integration.post_integration_integration_name_add(integration_name='notion', request_body=operations.PostIntegrationIntegrationNameAddRequestBody(
    brain_id='1f1d7a6a-e45b-4974-a0ba-98935650cb9c',
    page_ids=[
        '65621',
    ],
))

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                    | Type                                                                                                                                         | Required                                                                                                                                     | Description                                                                                                                                  | Example                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `integration_name`                                                                                                                           | *str*                                                                                                                                        | :heavy_check_mark:                                                                                                                           | Currently supported integrations are "notion" and "confluence". More integrations will be added in the future.                               | notion                                                                                                                                       |
| `request_body`                                                                                                                               | [Optional[operations.PostIntegrationIntegrationNameAddRequestBody]](../../models/operations/postintegrationintegrationnameaddrequestbody.md) | :heavy_minus_sign:                                                                                                                           | N/A                                                                                                                                          | {<br/>"brain_id": "1f1d7a6a-e45b-4974-a0ba-98935650cb9c",<br/>"page_ids": [<br/>"65621"<br/>]<br/>}                                          |


### Response

**[operations.PostIntegrationIntegrationNameAddResponse](../../models/operations/postintegrationintegrationnameaddresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
