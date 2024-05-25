"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from athenacopilotsdk import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostIntegrationIntegrationNameAddRequestBody:
    brain_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('brain_id'), 'exclude': lambda f: f is None }})
    r"""ID of the brain to add pages to"""
    page_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('page_ids'), 'exclude': lambda f: f is None }})
    r"""Array of page IDs to add to the brain"""
    



@dataclasses.dataclass
class PostIntegrationIntegrationNameAddRequest:
    integration_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'integration_name', 'style': 'simple', 'explode': False }})
    r"""Currently supported integrations are \\"notion\\" and \\"confluence\\". More integrations will be added in the future."""
    request_body: Optional[PostIntegrationIntegrationNameAddRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostIntegrationIntegrationNameAddResponseBody:
    r"""OK"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""Message indicating the pages are being added to the brain"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostIntegrationIntegrationNameAddResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    headers: Dict[str, List[str]] = dataclasses.field()
    object: Optional[PostIntegrationIntegrationNameAddResponseBody] = dataclasses.field(default=None)
    r"""OK"""
    

