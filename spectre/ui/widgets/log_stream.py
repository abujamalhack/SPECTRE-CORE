from textual.widgets import Static
from spectre.core.fake_intel import IntelEngine
from spectre.core.threat_engine import ThreatEngine

class LogStreamWidget(Static):
    def __init__(self):
        super().__init__("")
        self.intel = IntelEngine()
        self.threat = ThreatEngine()
        self.logs = []
    def push_log(self):
        self.logs.append(self.intel.generate_report())
        self.logs.append(self.threat.scan())
        if len(self.logs) > 15:
            self.logs = self.logs[-15:]
        self.update("\n".join(self.logs))
    def write(self, msg):
        self.logs.append(msg)
        self.update("\n".join(self.logs))
