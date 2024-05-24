"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from athenacopilotsdk import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostBrainRequestBody:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name of the brain"""
    



@dataclasses.dataclass
class PostBrainResponseBody:
    r"""OK"""
    



@dataclasses.dataclass
class PostBrainResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    headers: Dict[str, List[str]] = dataclasses.field()
    object: Optional[PostBrainResponseBody] = dataclasses.field(default=None)
    r"""OK"""
    
