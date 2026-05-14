from rich.prompt import Prompt
from rich.console import Console

class LoginScreen:
    def __init__(self, console):
        self.console = console
    async def prompt(self):
        self.console.print("[bold magenta]>> CLASSIFIED ACCESS <<[/bold magenta]")
        Prompt.ask("Enter cipher channel ID")
        Prompt.ask("Session key")
        Prompt.ask("Access token")
        self.console.print("[green]Authentication simulated... GRANTED[/green]")
        return {"user": "agent_shadow", "clearance": "OMEGA-7"}
