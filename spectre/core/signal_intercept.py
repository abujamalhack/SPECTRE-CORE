"""Fake signal interception."""
import random, time
def intercept() -> str:
    freq = f"{random.uniform(400, 6000):.2f} MHz"
    proto = random.choice(['GSM','LTE','5G NR','SATCOM'])
    return f"INTERCEPT {freq} {proto} RSSI:{random.randint(-90,-40)} dBm"
