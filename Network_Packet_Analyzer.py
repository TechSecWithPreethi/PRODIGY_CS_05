from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

# Packet analysis function
def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        protocol = "TCP" if TCP in packet else "UDP" if UDP in packet else "Other"
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        print(f"Protocol: {protocol}")
        print(f"Payload: {bytes(packet[TCP].payload) if TCP in packet else bytes(packet[UDP].payload) if UDP in packet else 'N/A'}")
        print("="*40)

# Sniff packets at Layer 3
sniff(prn=packet_callback, count=10, filter="ip")  # Adjust count as needed
