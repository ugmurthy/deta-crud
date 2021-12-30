from pydantic import BaseModel
from typing import Optional

## all readings in device collection
class Reading(BaseModel):
    packet: int
    SeqNo: int
    secs: float
    AccX: float
    AccY: float
    AccZ: float
    rms: float
    dpeak: int 
    peak: int 

# header is stored in headers collections
class Header(BaseModel):
    Version: str
    Device: str
    period: int 
    ontime: int 
    timestamp: str 
    location: str 
    activity: str 

