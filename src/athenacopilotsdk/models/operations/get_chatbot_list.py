"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import chatbotresponse as components_chatbotresponse
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from typing import Dict, List, Optional


@dataclasses.dataclass
class GetChatbotListRequest:
    brain_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'brain_id', 'style': 'form', 'explode': True }})
    r"""The ID of the brain to filter chatbots"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetChatbotListResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    headers: Dict[str, List[str]] = dataclasses.field()
    chatbot_responses: Optional[List[components_chatbotresponse.ChatbotResponse]] = dataclasses.field(default=None)
    r"""OK"""
    
