"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from athenacopilotsdk import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutBrainBrainIDRequestBody:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Updated name of the brain"""
    



@dataclasses.dataclass
class PutBrainBrainIDRequest:
    brain_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'brain_id', 'style': 'simple', 'explode': False }})
    request_body: Optional[PutBrainBrainIDRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class PutBrainBrainIDResponseBody:
    r"""OK"""
    



@dataclasses.dataclass
class PutBrainBrainIDResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    headers: Dict[str, List[str]] = dataclasses.field()
    object: Optional[PutBrainBrainIDResponseBody] = dataclasses.field(default=None)
    r"""OK"""
    
