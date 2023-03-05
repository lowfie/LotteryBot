from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class Operation(BaseModel):
    operation_id: str = None
    status: str = None
    datetime: str = None
    title: str = None
    pattern_id: str = None
    direction: str = None
    amount: float = None
    label: str = None
    operation_type: str = None
    type: str = None


class Payload(BaseModel):
    type: str = None
    label: str = None
    from_date: Optional[datetime] = None
    till_date: Optional[datetime] = None
    start_record: str = None
    records: int = None
    details: bool = None
