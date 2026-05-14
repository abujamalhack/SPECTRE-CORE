import random
def glitch_text(text, intensity=0.2):
    """Simulate glitch by swapping characters randomly."""
    chars = list(text)
    for i in range(len(chars)):
        if random.random() < intensity:
            chars[i] = random.choice('!@#$%&*0123456789')
    return ''.join(chars)
