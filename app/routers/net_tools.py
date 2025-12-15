import ipaddress
import socket
import struct
from fastapi import APIRouter
from app.schemas.belongs import BelongsRequest

router = APIRouter(prefix="/net", tags=["Network Tools"])

@router.get("/belongs/{ip}/{network_ip}/{bits}")
def belongs(ip: str, network_ip: str, bits: int):
    return {
        "belongs": ipaddress.ip_address(ip)
        in ipaddress.ip_network(f"{network_ip}/{bits}", strict=False)
    }

@router.post("/belongs")
def belongs_post(data: BelongsRequest):
    return {
        "belongs": ipaddress.ip_address(data.ip)
        in ipaddress.ip_network(f"{data.network_ip}/{data.bits}", strict=False)
    }

@router.get("/local-ip")
def local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return {"local_ip": ip}

@router.get("/gateway")
def gateway():
    with open("/proc/net/route") as f:
        for line in f.readlines()[1:]:
            fields = line.split()
            if fields[1] == "00000000":
                gw = socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))
                return {"gateway": gw}
    return {"gateway": None}
