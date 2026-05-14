"""Simulated threat detection engine."""
import random
from spectre.utils.fake_data import threat_actors

class ThreatEngine:
    def scan(self) -> str:
        actor = random.choice(threat_actors)
        severity = random.choice(['LOW','MEDIUM','HIGH','CRITICAL'])
        return f"THREAT DETECTED: {actor} | SEVERITY: {severity}"
