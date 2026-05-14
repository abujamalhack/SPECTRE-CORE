"""Generates fake intelligence reports, alerts, and target profiles."""
import random
import time
from spectre.utils.fake_data import fake_names, fake_phones, fake_countries

class IntelEngine:
    def generate_report(self) -> str:
        target = random.choice(fake_names)
        phone = random.choice(fake_phones)
        country = random.choice(fake_countries)
        return (
            f"INTEL [{time.strftime('%H:%M:%S')}] "
            f"TARGET: {target} | PHONE: {phone} | LOC: {country} | "
            f"THREAT LEVEL: {'CRITICAL' if random.random()>0.7 else 'ELEVATED'}"
        )
