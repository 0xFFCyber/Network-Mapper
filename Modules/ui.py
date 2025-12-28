from rich.tree import Tree
from rich.console import Console

console = Console()

def render_map(local_ip, network_map):
    tree = Tree(f"[bold cyan]This Device : ({local_ip})")

    for device_ip, protocols in network_map.items():
        node = tree.add(f"[bold yellow]{device_ip}")
        for protocol, count in protocols.items():
            if count == 1:
                node.add(f"{protocol} : {count} packet 📦")
            else:
                node.add(f"{protocol} : {count} packets 📦")
                
    console.clear()
    console.print(tree)