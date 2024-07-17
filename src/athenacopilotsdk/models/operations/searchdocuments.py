"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import document as components_document
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclasses.dataclass
class SearchDocumentsRequest:
    brain_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'brain_id', 'style': 'simple', 'explode': False }})
    r"""ID of the brain to search in"""
    search_query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'search_query', 'style': 'form', 'explode': True }})
    r"""Optional search query to filter documents"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchDocumentsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    documents: Optional[List[components_document.Document]] = dataclasses.field(default=None)
    r"""Successful search operation"""
    
