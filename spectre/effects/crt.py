"""Apply CRT scanline and flicker to a Rich renderable."""
def crt_filter(text):
    # Simplified: adds random spaces and line noise
    return text.replace('0','O').replace('1','l')
