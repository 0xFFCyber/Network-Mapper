from scapy.all import TCP,UDP,IP,ARP
from collections import defaultdict

class Network_Map():
    def __init__(self, local_ip):
        self.local_ip = local_ip
        self.map = defaultdict(lambda: defaultdict(int))
    
    def process(self, packet):
        if IP not in packet:
            return
        
        src = packet[IP].src
        dst = packet[IP].dst

        if src == self.local_ip:
            other_device = dst
        elif dst == self.local_ip:
            other_device = src
        else:
            return # The packet doesnt interest us
        
        protocol_ip = self.get_protocol(packet)
        self.map[other_device][protocol_ip]+=1

    def get_protocol(self, packet):

        if packet.haslayer(TCP):
            return("[bold magenta]TCP")
        elif packet.haslayer(UDP):
            return("[bold red]UDP")
        elif packet.haslayer(ARP):
            return("[bold orange]ARP")
        else:
            return("Unknown Protocol")
        


    
