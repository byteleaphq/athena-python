"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import documentreviewdetail as components_documentreviewdetail
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclasses.dataclass
class ListDocumentReviewsRequest:
    brain_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'brain_id', 'style': 'form', 'explode': True }})
    r"""Optional brain ID to filter document reviews"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListDocumentReviewsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    document_review_details: Optional[List[components_documentreviewdetail.DocumentReviewDetail]] = dataclasses.field(default=None)
    r"""Successful retrieval of document reviews"""
    

