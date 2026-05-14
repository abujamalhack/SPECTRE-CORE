import asyncio, random, time
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.text import Text
from spectre.effects.glitch import glitch_text
from spectre.animations.typing import type_out

class BootSequence:
    def __init__(self, console):
        self.console = console
    async def run(self):
        lines = [
            "SPECTRE BIOS v9.0 // J.C.W.D OMEGA-7",
            "INITIALIZING HARDWARE TOKEN... OK",
            "ENCRYPTED MEMORY TEST... PASSED",
            "QUANTUM KEY EXCHANGE... ESTABLISHED",
            "SATELLITE UPLINK: USA-274 LOCK",
            "THREAT CORE LOADING...████████████ 100%",
            "DARKNET RELAY SYNC... ACTIVE",
            "AI ASSISTANT ONLINE",
            "BOOT SEQUENCE COMPLETE"
        ]
        with Live(Panel("", title="BOOT"), refresh_per_second=10) as live:
            for line in lines:
                glitched = glitch_text(line, intensity=0.3)
                live.update(Panel(Text(glitched, style="bold purple"), title="BOOT"))
                await asyncio.sleep(random.uniform(0.3, 0.8))
        self.console.clear()
