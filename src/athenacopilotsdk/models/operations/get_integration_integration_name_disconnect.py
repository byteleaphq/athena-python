"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata


@dataclasses.dataclass
class GetIntegrationIntegrationNameDisconnectRequest:
    integration_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'integration_name', 'style': 'simple', 'explode': False }})
    r"""Currently supported integrations are \\"notion\\" and \\"confluence\\". More integrations will be added in the future."""
    



@dataclasses.dataclass
class GetIntegrationIntegrationNameDisconnectResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    

