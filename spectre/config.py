"""Global configuration for SPECTRE-CORE."""
from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class Config:
    app_name: str = "SPECTRE-CORE v9.0"
    codename: str = "GHOST_PROTOCOL"
    clearance_level: str = "OMEGA-7"
    fake_agency: str = "Joint Cyber Warfare Division"
    theme: str = "cyberpunk_military"
    fps: int = 30
    log_verbosity: int = 3
    fake_ips: list = field(default_factory=lambda: [
        "192.168.7.14", "10.4.2.99", "172.20.0.13", "44.233.18.7"
    ])
    fake_macs: list = field(default_factory=lambda: [
        "00:1A:79:4C:BB:23", "08:94:EF:33:7A:11", "F4:8C:50:0E:9D:A0"
    ])
