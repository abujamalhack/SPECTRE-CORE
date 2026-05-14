"""Fake AI assistant with canned responses."""
responses = [
    "Analyzing threat vectors...",
    "Correlating signal intelligence...",
    "Mapping darknet topology...",
    "Identifying zero-day signatures...",
    "CROSS-REFERENCING GLOBAL DATABASE..."
]
def query() -> str:
    import random
    return random.choice(responses)
