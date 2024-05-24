"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from typing import Dict, List, Optional


@dataclasses.dataclass
class GetIntegrationIntegrationNameListRequest:
    integration_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'integration_name', 'style': 'simple', 'explode': False }})
    r"""Currently supported integrations are \\"notion\\" and \\"confluence\\". More integrations will be added in the future."""
    



@dataclasses.dataclass
class GetIntegrationIntegrationNameListResponseBody:
    r"""OK"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetIntegrationIntegrationNameListResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    headers: Dict[str, List[str]] = dataclasses.field()
    object: Optional[GetIntegrationIntegrationNameListResponseBody] = dataclasses.field(default=None)
    r"""OK"""
    

