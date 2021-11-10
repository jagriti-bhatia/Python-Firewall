#!/usr/bin/env python3

#running instructions
#chmod +x scap_sniff.py
#sudo ./scap_sniff.py

from scapy.all import *

import sys, signal
def signal_handler(signal, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


while True:
    a=sniff(count = 1) 
    #a.nsummary() 
    a[0].show()
    break
