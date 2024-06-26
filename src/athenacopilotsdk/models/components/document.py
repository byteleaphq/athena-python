"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from athenacopilotsdk import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Document:
    UNSET='__SPEAKEASY_UNSET__'
    chunk_header: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chunk_header'), 'exclude': lambda f: f is Document.UNSET }})
    r"""The header or context information for the document chunk."""
    content: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content'), 'exclude': lambda f: f is Document.UNSET }})
    r"""The content or text of the document chunk."""
    created_on: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_on'), 'exclude': lambda f: f is None }})
    r"""The Unix timestamp representing the creation time of the document."""
    description: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is Document.UNSET }})
    r"""The description or summary of the document."""
    document_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('document_type'), 'exclude': lambda f: f is None }})
    r"""The type of the document (e.g., raw_text, file, url)."""
    file_extension: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_extension'), 'exclude': lambda f: f is Document.UNSET }})
    r"""The file extension of the document (if applicable)."""
    file_name: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_name'), 'exclude': lambda f: f is Document.UNSET }})
    r"""The name of the file for the document (if applicable)."""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The unique identifier of the document."""
    knowledge_base_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('knowledge_base_id'), 'exclude': lambda f: f is None }})
    r"""The identifier of the knowledge base to which the document belongs."""
    link_to_source: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link_to_source'), 'exclude': lambda f: f is Document.UNSET }})
    r"""The URL or link to the source of the document (if applicable)."""
    supp_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supp_id'), 'exclude': lambda f: f is Document.UNSET }})
    r"""The supplementary identifier of the document (if applicable)."""
    title: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is Document.UNSET }})
    r"""The title of the document."""
    url: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is Document.UNSET }})
    r"""The URL of the document (if applicable)."""
    vectorization_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vectorization_status'), 'exclude': lambda f: f is None }})
    r"""The status of the document vectorization process."""
    total_chunks: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_chunks'), 'exclude': lambda f: f is Document.UNSET }})
    r"""The total number of chunks the document is divided into."""
    

