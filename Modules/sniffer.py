from scapy.all import sniff

def start_sniff(callback):
    sniff(prn=callback, store=False) # No storage to save ram & privacy