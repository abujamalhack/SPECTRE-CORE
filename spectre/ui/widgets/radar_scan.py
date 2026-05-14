from textual.widgets import Static
import math, time

class RadarWidget(Static):
    def __init__(self):
        super().__init__("")
        self.angle = 0
    def spin(self):
        self.angle = (self.angle + 5) % 360
        rad = math.radians(self.angle)
        line = int(10 + 8 * math.cos(rad))
        art = f"RADAR SWEEP {self.angle}°\n" + "█" * line
        self.update(art)
