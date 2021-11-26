import struct
import socket
import binascii

def mac_addr(mac_add_bytes):
    # convert the bytes to string
    return ':'.join(map('{:02x}'.format, mac_add_bytes)).upper()


def ethernet_frame(data):
    dest_mac, src_mac, eth_protocol = struct.unpack('!6s6sH', data[:14])
    return mac_addr(dest_mac), mac_addr(src_mac), socket.htons(eth_protocol), data[14:]


def ipv4_packet(ip_header):
    iph = struct.unpack('!BBHHHBBH4s4s', ip_header[:20])

    protocol = iph[6]

    s_addr = iph[8]
    d_addr = iph[9]

    return format_ipv4(s_addr),format_ipv4(d_addr), protocol

def format_ipv4(addr):
    return '.'.join(map(str,addr))

def tcp_packet(packet_buffer):
    tcp_raw_data = struct.unpack("!HH", packet_buffer[0:4])
    src_port = tcp_raw_data[0]
    dst_port = tcp_raw_data[1]

    return src_port, dst_port

def udp_packet(data):
    src_port, dest_port = struct.unpack('!HH', data)
    return src_port, dest_port
