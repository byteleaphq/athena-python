# Document
(*document*)

### Available Operations

* [create_text_document](#create_text_document) - Create Text Document
* [create_url_document](#create_url_document) - Create Document by URL
* [download_document](#download_document) - Download
* [get_all_documents](#get_all_documents) - List Documents
* [get_document_by_id](#get_document_by_id) - Get Document
* [delete_document](#delete_document) - Delete Document
* [upload_document](#upload_document) - Upload Document

## create_text_document

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


res = s.document.create_text_document(brain_id='{{brain_id}}', request_body=operations.CreateTextDocumentRequestBody(
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
| `request_body`                                                                                                                                                                                                                        | [Optional[operations.CreateTextDocumentRequestBody]](../../models/operations/createtextdocumentrequestbody.md)                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                   | {<br/>"content": "What is an operating system? An operating system (OS) is the program that, after being initially loaded into the computer by a boot program, manages all of the other application programs in a computer............"<br/>} |


### Response

**[operations.CreateTextDocumentResponse](../../models/operations/createtextdocumentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create_url_document

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


res = s.document.create_url_document(brain_id='{{brain_id}}', request_body=operations.CreateURLDocumentRequestBody(
    url='https://en.wikipedia.org/wiki/Artificial_intelligence',
))

if res.document is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  | Example                                                                                                      |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `brain_id`                                                                                                   | *str*                                                                                                        | :heavy_check_mark:                                                                                           | N/A                                                                                                          | {{brain_id}}                                                                                                 |
| `request_body`                                                                                               | [Optional[operations.CreateURLDocumentRequestBody]](../../models/operations/createurldocumentrequestbody.md) | :heavy_minus_sign:                                                                                           | N/A                                                                                                          | {<br/>"url": "https://en.wikipedia.org/wiki/Artificial_intelligence"<br/>}                                   |


### Response

**[operations.CreateURLDocumentResponse](../../models/operations/createurldocumentresponse.md)**
### Errors

| Error Object                         | Status Code                          | Content Type                         |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| errors.CreateURLDocumentResponseBody | 500                                  | application/json                     |
| errors.SDKError                      | 4xx-5xx                              | */*                                  |

## download_document

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


res = s.document.download_document(brain_id='{{brain_id}}', document_id='a00f07cb-c04c-4824-9b26-5b7eb5c274ae')

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

**[operations.DownloadDocumentResponse](../../models/operations/downloaddocumentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_all_documents

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


res = s.document.get_all_documents(brain_id='{{brain_id}}')

if res.documents is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `brain_id`         | *str*              | :heavy_check_mark: | N/A                | {{brain_id}}       |


### Response

**[operations.GetAllDocumentsResponse](../../models/operations/getalldocumentsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## get_document_by_id

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


res = s.document.get_document_by_id(brain_id='{{brain_id}}', document_id='020d69cb-197b-47ef-911b-ee45ee260839')

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

**[operations.GetDocumentByIDResponse](../../models/operations/getdocumentbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## delete_document

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


res = s.document.delete_document(brain_id='{{brain_id}}', document_id='5ca417c0-6d74-4752-a9cd-e2813ea67fd6')

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

**[operations.DeleteDocumentResponse](../../models/operations/deletedocumentresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## upload_document

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


res = s.document.upload_document(brain_id='<value>', request_body=operations.UploadDocumentRequestBody())

if res.document is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `brain_id`                                                                                             | *str*                                                                                                  | :heavy_check_mark:                                                                                     | The ID of the knowledge base to which the document belongs                                             |
| `request_body`                                                                                         | [Optional[operations.UploadDocumentRequestBody]](../../models/operations/uploaddocumentrequestbody.md) | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |


### Response

**[operations.UploadDocumentResponse](../../models/operations/uploaddocumentresponse.md)**
### Errors

| Error Object                              | Status Code                               | Content Type                              |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| errors.UploadDocumentResponseBody         | 400                                       | application/json                          |
| errors.UploadDocumentDocumentResponseBody | 500                                       | application/json                          |
| errors.SDKError                           | 4xx-5xx                                   | */*                                       |
