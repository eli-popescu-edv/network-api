import ipaddress
from fastapi import APIRouter
from app.schemas.subnet import SubnetRequest

router = APIRouter(prefix="/subnet", tags=["Subnet Calculator"])

@router.get("/{ip}/{bits}")
def calc_subnet(ip: str, bits: int):
    net = ipaddress.ip_network(f"{ip}/{bits}", strict=False)

    first = net.network_address if bits >= 31 else net.network_address + 1
    last = net.broadcast_address if bits >= 31 else net.broadcast_address - 1

    return {
        "ip": ip,
        "bits": bits,
        "mask": str(net.netmask),
        "network": str(net.network_address),
        "broadcast": str(net.broadcast_address),
        "range": f"{first} - {last}",
    }

@router.post("/calculate")
def calc_subnet_post(data: SubnetRequest):
    net = ipaddress.ip_network(f"{data.ip}/{data.bits}", strict=False)

    first = net.network_address if data.bits >= 31 else net.network_address + 1
    last = net.broadcast_address if data.bits >= 31 else net.broadcast_address - 1

    return {
        "ip": data.ip,
        "bits": data.bits,
        "mask": str(net.netmask),
        "network": str(net.network_address),
        "broadcast": str(net.broadcast_address),
        "range": f"{first} - {last}",
    }

@router.get("/mask/{bits}")
def get_mask(bits: int):
    net = ipaddress.ip_network(f"0.0.0.0/{bits}")
    return {"bits": bits, "mask": str(net.netmask)}

@router.get("/addresses/{ip}/{bits}")
def addresses(ip: str, bits: int):
    net = ipaddress.ip_network(f"{ip}/{bits}", strict=False)
    return {
        "network": str(net.network_address),
        "broadcast": str(net.broadcast_address),
    }
