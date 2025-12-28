# Network-Mapper by 0xFFCyber (Open-Source)
# This was made for curiosity only this is not a real project


# === Hierarchy ===

# Network-Mapper/
# | main.py
# | README.md
# | Modules/
# |     analyze.py
# |     sniffer.py
# |     ui.py



import os 
import sys

if os.geteuid() !=0:
    print("This program have not been launched using sudo/administrator")
    sys.exit(1)

import time
import threading
from scapy.all import get_if_addr
from rich.console import Console
from Modules.sniffer import start_sniff
from Modules.analyze import Network_Map
from Modules.ui import render_map
console = Console()

# ==== CHOIX DE L'INTERFACE ====
console.clear()
print("Program launched as administrator ✅")
print("Please choose the interface to map")
print("1 / Wi-Fi 🛜")
print("2 / Ethernet 🔒")

interfacechoice = input("\n> ")

if interfacechoice == ("1"):
    INTERFACE = "en0"
elif interfacechoice == ("2"):
    INTERFACE = "en1"
else:
    print("Error Syntax")
    sys.exit(1)


local_ip = get_if_addr(INTERFACE)
network_map = Network_Map(local_ip)


def on_each_packet(packet):
    network_map.process(packet)


sniffer_thread = threading.Thread(target=start_sniff, args=(on_each_packet,), daemon=True) # on_each_packet is a tuple
sniffer_thread.start()

while True:
    render_map(local_ip, network_map.map)
    time.sleep(1)

