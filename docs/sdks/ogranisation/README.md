# Ogranisation
(*ogranisation*)

### Available Operations

* [get_organisation_](#get_organisation_) - get user org

## get_organisation_

get user org

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


res = s.ogranisation.get_organisation_()

if res.object is not None:
    # handle response
    pass

```


### Response

**[operations.GetOrganisationResponse](../../models/operations/getorganisationresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
