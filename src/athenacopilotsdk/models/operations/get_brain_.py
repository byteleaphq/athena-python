"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from typing import Dict, List, Optional


@dataclasses.dataclass
class GetBrainResponseBody:
    r"""OK"""
    



@dataclasses.dataclass
class GetBrainResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    headers: Dict[str, List[str]] = dataclasses.field()
    object: Optional[GetBrainResponseBody] = dataclasses.field(default=None)
    r"""OK"""
    

