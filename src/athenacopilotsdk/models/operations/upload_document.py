"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import document as components_document
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class File:
    file_name: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'file' }})
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})
    



@dataclasses.dataclass
class UploadDocumentRequestBody:
    file: Optional[File] = dataclasses.field(default=None, metadata={'multipart_form': { 'file': True }})
    



@dataclasses.dataclass
class UploadDocumentRequest:
    brain_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'brain_id', 'style': 'simple', 'explode': False }})
    r"""The ID of the knowledge base to which the document belongs"""
    request_body: Optional[UploadDocumentRequestBody] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UploadDocumentResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    document: Optional[components_document.Document] = dataclasses.field(default=None)
    r"""OK"""
    
