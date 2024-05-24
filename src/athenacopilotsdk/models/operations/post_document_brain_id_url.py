"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from athenacopilotsdk import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostDocumentBrainIDURLRequestBody:
    url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is None }})
    r"""Url of the website that you want to add"""
    



@dataclasses.dataclass
class PostDocumentBrainIDURLRequest:
    brain_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'brain_id', 'style': 'simple', 'explode': False }})
    request_body: Optional[PostDocumentBrainIDURLRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class PostDocumentBrainIDURLResponseBody:
    r"""OK"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostDocumentBrainIDURLResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    headers: Dict[str, List[str]] = dataclasses.field()
    object: Optional[PostDocumentBrainIDURLResponseBody] = dataclasses.field(default=None)
    r"""OK"""
    

