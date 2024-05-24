"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from athenacopilotsdk import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Dict, List, Optional


@dataclasses.dataclass
class DeleteBrainBrainIDRequest:
    brain_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'brain_id', 'style': 'simple', 'explode': False }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteBrainBrainIDResponseBody:
    r"""OK"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteBrainBrainIDResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    headers: Dict[str, List[str]] = dataclasses.field()
    object: Optional[DeleteBrainBrainIDResponseBody] = dataclasses.field(default=None)
    r"""OK"""
    

