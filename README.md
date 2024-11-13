# PRODIGY_CS_05
A Python tool for capturing and analyzing network packets, displaying source and destination IPs, protocols, and payload data. Developed for ethical and educational use.

# Description

This Python code creates a packet sniffer using the " scapy " library. It listens to network traffic and captures network packets, displaying essential details like source and destination IP addresses, protocol type (TCP, UDP, or other), and payload data. This tool can be useful for analyzing network behavior, understanding packet structures, and learning network security concepts.

# Working of the Code

1. Imports:
    - sniff: ---------------> Function to capture packets.
    - IP, TCP, UDP: --------> Classes for identifying and accessing IP, TCP, and UDP packet layers.

2. Packet Analysis Function (packet_callback):
    - This function is called for each packet captured.
    - Checks if the packet contains an IP layer.
    - Determines if the protocol is TCP or UDP (or "Other" if neither).
    - Prints the source and destination IP addresses, protocol type, and payload data (if present).

3. Packet Capture:
- sniff(prn=packet_callback, count=10, filter="ip"): --------> Captures 10 IP packets and calls packet_callback for each packet.

# Requirements

1. To run this code, install the Scapy library and Npcap (on Windows) or tcpdump (on Linux).

- Install Scapy:

pip install scapy

- Install Npcap (for Windows users) or tcpdump (for Linux):

* Npcap: Download and install from Npcap's website.
* tcpdump: Install via package manager, e.g., sudo apt-get install tcpdump on Linux.

# Use and Purpose

This tool provides a basic, ethical way to observe network traffic for educational purposes, helping users understand networking protocols and packet structures. It’s ideal for beginners interested in network security and traffic analysis.
