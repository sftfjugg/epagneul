import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class BaseEvent(BaseModel):
    source: str
    target: str
    timestamps: set = set()
    event_type: int

    class Config:
        extra = "allow"


class LogonEvent(BaseEvent):
    timestamp: datetime.datetime


class NativeLogonEvent(LogonEvent):
    logon_type: int = 0
    status: str = ""


class SysmonLogonEvent(LogonEvent):
    initiated: Optional[bool]
    image: Optional[str]
    procotol: Optional[str]
    destination_port: Optional[int]
    source_port: Optional[int]


class EventInDB(BaseEvent):
    tip: str
    count: int = 1
    id: Optional[UUID]
