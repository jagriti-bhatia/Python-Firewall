#import random
#import time
import struct
import socket
import binascii

def mac_addr(mac_add_bytes):
    # convert the bytes to string
    return ':'.join(map('{:02x}'.format, mac_add_bytes)).upper()


def ethernet_frame(data):
    dest_mac, src_mac, eth_protocol = struct.unpack('!6s6sH', data[:14])
    return mac_addr(dest_mac), mac_addr(src_mac), socket.htons(eth_protocol), data


def ipv4_packet(ip_header):
    iph = struct.unpack('!BBHHHBBH4s4s', ip_header[:20])

    protocol = iph[6]

    s_addr = socket.inet_ntoa(iph[8])
    d_addr = socket.inet_ntoa(iph[9])

    return s_addr, d_addr, protocol

def tcp_packet(packet_buffer):
    tcp_raw_data = struct.unpack("!2s2s4s4s2s2s2s2s", packet_buffer)
    src_port = binary_to_ascii(tcp_raw_data[0])
    dst_port = binary_to_ascii(tcp_raw_data[1])

    return int(src_port, 16), int(dst_port, 16)

def binary_to_ascii(binary_data):
    return binascii.hexlify(binary_data).decode("utf-8")

def udp_packet(data):
    src_port, dest_port, size = struct.unpack('!HH2xH', data)
    return src_port, dest_port, size, data[8:]