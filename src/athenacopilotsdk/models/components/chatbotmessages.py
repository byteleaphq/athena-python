"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .document import Document
from athenacopilotsdk import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional, Union


@dataclasses.dataclass
class Reference2:
    pass

ChatbotMessagesReference = Union[Document, 'Reference2']


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ChatMessages:
    UNSET='__SPEAKEASY_UNSET__'
    actor: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('actor'), 'exclude': lambda f: f is None }})
    r"""The actor of the message, either USER or AI"""
    created_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'exclude': lambda f: f is None }})
    r"""The timestamp when the message was created"""
    id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""The ID of the message"""
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})
    r"""The content of the message"""
    reference: Optional[List[ChatbotMessagesReference]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference'), 'exclude': lambda f: f is ChatMessages.UNSET }})
    r"""The list of references associated with the interaction"""
    thread_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('thread_id'), 'exclude': lambda f: f is None }})
    r"""The ID of the thread the message belongs to"""
    timestamp: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestamp'), 'exclude': lambda f: f is ChatMessages.UNSET }})
    r"""The timestamp of the message, if available"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ChatbotMessages:
    chat_messages: Optional[List[ChatMessages]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chat_messages'), 'exclude': lambda f: f is None }})
    

