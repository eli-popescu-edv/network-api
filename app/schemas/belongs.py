from pydantic import BaseModel


class BelongsRequest(BaseModel):
    ip: str
    network_ip: str
    bits: int
