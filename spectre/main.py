#!/usr/bin/env python3
"""
SPECTRE-CORE Main Entry Point.
Simulates a classified cyber‑warfare terminal interface.
"""
import asyncio
from rich.console import Console
from spectre.ui.screens.boot import BootSequence
from spectre.ui.screens.login import LoginScreen
from spectre.ui.app import SpectreApp

async def main():
    console = Console()
    # --- Boot Sequence ---
    boot = BootSequence(console)
    await boot.run()

    # --- Fake Login ---
    login = LoginScreen(console)
    session = await login.prompt()

    # --- Launch Full Dashboard (Textual TUI) ---
    app = SpectreApp(session)
    await app.run_async()

if __name__ == "__main__":
    asyncio.run(main())
