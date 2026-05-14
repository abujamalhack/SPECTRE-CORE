"""
Main Textual application – dashboard with multiple panes.
Includes fake command console, radar, logs, and status.
"""
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Input, Log
from textual.containers import Container, Horizontal, Vertical
from textual.reactive import reactive
from spectre.ui.widgets.radar_scan import RadarWidget
from spectre.ui.widgets.status_panel import StatusWidget
from spectre.ui.widgets.log_stream import LogStreamWidget
from spectre.ui.widgets.animated_border import AnimatedBorder
from spectre.ui.screens.dashboard import DashboardScreen

class SpectreApp(App):
    CSS_PATH = None  # We'll use inline styles or Rich console markup, Textual CSS would be extensive.
    TITLE = "SPECTRE-CORE // CLASSIFIED OMEGA-7"

    def compose(self) -> ComposeResult:
        yield Header()
        # Main layout
        with Horizontal():
            with Vertical(id="left-panel"):
                yield StatusWidget()
                yield RadarWidget()
            with Vertical(id="center-panel"):
                yield LogStreamWidget()
                yield Input(placeholder="Enter command (e.g., /trace, /analyze) ...", id="cmd-input")
        yield Footer()

    def on_mount(self):
        # Start periodic refresh for live data
        self.set_interval(0.5, self.update_dashboard)

    def update_dashboard(self):
        # Push fresh data to widgets
        self.query_one(LogStreamWidget).push_log()
        self.query_one(RadarWidget).spin()

    def on_input_submitted(self, event: Input.Submitted):
        cmd = event.value.strip()
        # Fake command handling
        fake_output = f"Executing {cmd}...\n[cyan]FAKE OUTPUT: Operation simulated successfully.[/cyan]"
        self.query_one(LogStreamWidget).write(fake_output)
        event.input.value = ""
