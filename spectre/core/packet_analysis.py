"""Fake packet sniffer output."""
import random
def capture_packet() -> str:
    ips = ["10.7.3.22","172.20.99.1","44.235.18.9"]
    return (
        f"PKT {random.choice(ips)}:{random.randint(1024,65535)} -> "
        f"{random.choice(ips)}:{random.randint(80,443)} "
        f"PROTO:TCP LEN:{random.randint(40,1500)}"
    )
