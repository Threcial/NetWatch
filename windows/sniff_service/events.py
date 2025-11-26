#数据结构定义

from dataclasses import dataclass
from datetime import datetime
from typing import Literal, Optional

EventType = Literal["new_device"]

@dataclass
class DeviceEvent:
    type: EventType
    time: datetime
    mac: str
    ip: Optional[str]
    info: str