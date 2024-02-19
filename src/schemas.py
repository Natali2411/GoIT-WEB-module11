from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, Field, PastDate


class ChannelModel(BaseModel):
    name: str = Field(max_length=50)


class ChannelResponse(ChannelModel):
    id: int

    class Config:
        orm_mode = True


class ContactChannelModel(BaseModel):
    contact_id: int
    channel_id: int
    channel_value: str


class ContactChannelResponse(ContactChannelModel):
    id: int

    class Config:
        orm_mode = True


class ContactModel(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    birthdate: PastDate
    gender: str = Field(max_length=1, examples=["F", "M"])
    persuasion: str = Field(max_length=50)
    created_at: datetime


class ContactResponse(ContactModel):
    id: int

    class Config:
        orm_mode = True
