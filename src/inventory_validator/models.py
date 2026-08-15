from typing import Literal
from pydantic import BaseModel, IPvAnyAddress, Field






Role   = Literal["pe", "p", "bng", "rr", "core"]
OsType = Literal["sros", "srlinux", "iosxr"]

class Device(BaseModel):
    name: str = Field(min_length=1)
    mgmt_ip: IPvAnyAddress
    role: Role
    os: OsType



class Inventory(BaseModel):
    devices: list[Device]

    