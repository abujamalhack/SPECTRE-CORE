"""Fake satellite uplink and signal tracing."""
import random
import math
import time

class SatelliteLink:
    def __init__(self):
        self.azimuth = 0
    def get_telemetry(self) -> dict:
        self.azimuth = (self.azimuth + 2) % 360
        return {
            "sat": "USA-274",
            "az": self.azimuth,
            "el": random.randint(10, 80),
            "sig_strength": random.randint(-60, -20),
            "data_rate": f"{random.randint(2,10)} Mbps"
        }
