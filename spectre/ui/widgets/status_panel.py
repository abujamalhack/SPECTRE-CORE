from textual.widgets import Static
import random, time

class StatusWidget(Static):
    def render(self):
        cpu = random.randint(20, 98)
        mem = random.randint(30, 92)
        temp = random.randint(45, 85)
        return (
            f"CPU: {cpu}% | MEM: {mem}% | TEMP: {temp}°C\n"
            f"UPLINK: SATCOM ACTIVE | THREAT LEVEL: ELEVATED"
        )
