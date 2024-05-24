<!-- Start SDK Example Usage [usage] -->
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
<!-- End SDK Example Usage [usage] -->