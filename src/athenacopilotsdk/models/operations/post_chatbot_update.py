"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from athenacopilotsdk import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostChatbotUpdateRequestBody:
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""The name of the chatbot"""
    urls: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('urls'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class PostChatbotUpdateResponseBody:
    r"""OK"""
    



@dataclasses.dataclass
class PostChatbotUpdateResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    headers: Dict[str, List[str]] = dataclasses.field()
    object: Optional[PostChatbotUpdateResponseBody] = dataclasses.field(default=None)
    r"""OK"""
    

