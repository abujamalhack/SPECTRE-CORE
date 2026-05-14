import asyncio, random
async def type_out(console, text, style="bold cyan"):
    for char in text:
        console.print(char, end='', style=style)
        await asyncio.sleep(random.uniform(0.02, 0.08))
    console.print()
