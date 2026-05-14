"""Fake darknet relay mapping."""
import random
from spectre.utils.fake_data import fake_ips

class DarknetMapper:
    def generate_nodes(self, num=12):
        nodes = []
        for i in range(num):
            nodes.append({
                "id": f"node-{i}",
                "ip": random.choice(fake_ips),
                "relay": random.choice(['Tor','I2P','ZeroNet','Lokinet']),
                "status": random.choice(['ACTIVE','DORMANT','COMPROMISED'])
            })
        return nodes
