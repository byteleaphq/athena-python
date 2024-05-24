"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from athenacopilotsdk import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Dict, List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutChatChatIDRequestBody:
    temperature: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('temperature'), 'exclude': lambda f: f is None }})
    r"""between 1 and 0"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""The updated name of the chat"""
    system_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('system_message'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class PutChatChatIDRequest:
    chat_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'chat_id', 'style': 'simple', 'explode': False }})
    request_body: Optional[PutChatChatIDRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class PutChatChatIDResponseBody:
    r"""OK"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PutChatChatIDResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    headers: Dict[str, List[str]] = dataclasses.field()
    object: Optional[PutChatChatIDResponseBody] = dataclasses.field(default=None)
    r"""OK"""
    

