# Document
(*document*)

### Available Operations

* [post_document_brain_id_text](#post_document_brain_id_text) - Create Text Document
* [post_document_brain_id_url](#post_document_brain_id_url) - Create Document by URL
* [get_document_brain_id_document_id_download](#get_document_brain_id_document_id_download) - Download
* [get_document_brain_id_](#get_document_brain_id_) - List Documents
* [get_document_brain_id_document_id_](#get_document_brain_id_document_id_) - Get Document
* [delete_document_brain_id_document_id_](#delete_document_brain_id_document_id_) - Delete Document
* [post_document_brain_id_file](#post_document_brain_id_file) - Upload Document

## post_document_brain_id_text

Create Text Document

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


res = s.document.post_document_brain_id_text(brain_id='{{brain_id}}', request_body=operations.PostDocumentBrainIDTextRequestBody(
    content='What is an operating system? An operating system (OS) is the program that, after being initially loaded into the computer by a boot program, manages all of the other application programs in a computer............',
))

if res.document is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                           | Example                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `brain_id`                                                                                                                                                                                                                            | *str*                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   | {{brain_id}}                                                                                                                                                                                                                          |
| `request_body`                                                                                                                                                                                                                        | [Optional[operations.PostDocumentBrainIDTextRequestBody]](../../models/operations/postdocumentbrainidtextrequestbody.md)                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   | {<br/>"content": "What is an operating system? An operating system (OS) is the program that, after being initially loaded into the computer by a boot program, manages all of the other application programs in a computer............"<br/>} |


### Response

**[operations.PostDocumentBrainIDTextResponse](../../models/operations/postdocumentbrainidtextresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## post_document_brain_id_url

Create Document by URL

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


res = s.document.post_document_brain_id_url(brain_id='{{brain_id}}', request_body=operations.PostDocumentBrainIDURLRequestBody(
    url='https://en.wikipedia.org/wiki/Artificial_intelligence',
))

if res.document is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            | Example                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `brain_id`                                                                                                             | *str*                                                                                                                  | :heavy_check_mark:                                                                                                     | N/A                                                                                                                    | {{brain_id}}                                                                                                           |
| `request_body`                                                                                                         | [Optional[operations.PostDocumentBrainIDURLRequestBody]](../../models/operations/postdocumentbrainidurlrequestbody.md) | :heavy_minus_sign:                                                                                                     | N/A                                                                                                                    | {<br/>"url": "https://en.wikipedia.org/wiki/Artificial_intelligence"<br/>}                                             |


### Response

**[operations.PostDocumentBrainIDURLResponse](../../models/operations/postdocumentbrainidurlresponse.md)**
### Errors

| Error Object                              | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| errors.PostDocumentBrainIDURLResponseBody | 500                                       | application/json                          |
| errors.SDKError                           | 4xx-5xx                                   | */*                                       |

## get_document_brain_id_document_id_download

Download

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


res = s.document.get_document_brain_id_document_id_download(brain_id='{{brain_id}}', document_id='a00f07cb-c04c-4824-9b26-5b7eb5c274ae')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `brain_id`                           | *str*                                | :heavy_check_mark:                   | N/A                                  | {{brain_id}}                         |
| `document_id`                        | *str*                                | :heavy_check_mark:                   | N/A                                  | a00f07cb-c04c-4824-9b26-5b7eb5c274ae |


### Response

**[operations.GetDocumentBrainIDDocumentIDDownloadResponse](../../models/operations/getdocumentbrainiddocumentiddownloadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_document_brain_id_

List Documents

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


res = s.document.get_document_brain_id_(brain_id='{{brain_id}}')

if res.documents is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `brain_id`         | *str*              | :heavy_check_mark: | N/A                | {{brain_id}}       |


### Response

**[operations.GetDocumentBrainIDResponse](../../models/operations/getdocumentbrainidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_document_brain_id_document_id_

Get Document

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


res = s.document.get_document_brain_id_document_id_(brain_id='{{brain_id}}', document_id='020d69cb-197b-47ef-911b-ee45ee260839')

if res.document is not None:
    # handle response
    pass

```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `brain_id`                           | *str*                                | :heavy_check_mark:                   | N/A                                  | {{brain_id}}                         |
| `document_id`                        | *str*                                | :heavy_check_mark:                   | N/A                                  | 020d69cb-197b-47ef-911b-ee45ee260839 |


### Response

**[operations.GetDocumentBrainIDDocumentIDResponse](../../models/operations/getdocumentbrainiddocumentidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_document_brain_id_document_id_

Delete Document

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


res = s.document.delete_document_brain_id_document_id_(brain_id='{{brain_id}}', document_id='5ca417c0-6d74-4752-a9cd-e2813ea67fd6')

if res.delete_response is not None:
    # handle response
    pass

```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `brain_id`                           | *str*                                | :heavy_check_mark:                   | N/A                                  | {{brain_id}}                         |
| `document_id`                        | *str*                                | :heavy_check_mark:                   | N/A                                  | 5ca417c0-6d74-4752-a9cd-e2813ea67fd6 |


### Response

**[operations.DeleteDocumentBrainIDDocumentIDResponse](../../models/operations/deletedocumentbrainiddocumentidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## post_document_brain_id_file

Upload Document

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


res = s.document.post_document_brain_id_file(brain_id='{{brain_id}}', request_body=operations.PostDocumentBrainIDFileRequestBody())

if res.document is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              | Example                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `brain_id`                                                                                                               | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | N/A                                                                                                                      | {{brain_id}}                                                                                                             |
| `request_body`                                                                                                           | [Optional[operations.PostDocumentBrainIDFileRequestBody]](../../models/operations/postdocumentbrainidfilerequestbody.md) | :heavy_minus_sign:                                                                                                       | N/A                                                                                                                      |                                                                                                                          |


### Response

**[operations.PostDocumentBrainIDFileResponse](../../models/operations/postdocumentbrainidfileresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
