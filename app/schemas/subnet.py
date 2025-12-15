from pydantic import BaseModel


class SubnetRequest(BaseModel):
    ip: str
    bits: int
