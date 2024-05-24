"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from typing import Dict, List, Optional


@dataclasses.dataclass
class GetChatbotAnalyticsRequest:
    chatbot_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'chatbot_id', 'style': 'form', 'explode': True }})
    



@dataclasses.dataclass
class GetChatbotAnalyticsResponseBody:
    r"""OK"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetChatbotAnalyticsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    headers: Dict[str, List[str]] = dataclasses.field()
    object: Optional[GetChatbotAnalyticsResponseBody] = dataclasses.field(default=None)
    r"""OK"""
    

