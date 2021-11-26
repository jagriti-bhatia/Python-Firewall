# importing modules
import socket
from netaddr import IPNetwork
import logging

# inporting custom modules
from imports.protocols import ethernet_frame, ipv4_packet, udp_packet, tcp_packet
from imports.helper import get_interfaces, PROTOCOLS
from imports.validator import validate_with_route_table

# to write into the log file
logging.basicConfig(level=logging.INFO, filename="firewall.log", filemode="w")

# creating a Send Socket
send_sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

def sendpacket(conn: socket.socket, payload, dst_ip):
    try:
        conn.sendto(payload, (dst_ip, 0))
    except PermissionError as broadcastError:
        print(broadcastError)
        pass


def bind_sockets(interface):
    # creating a socket connection to listen for packets
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW,socket.ntohs(0x0800))
    conn.bind((interface[0],0))
    try:
        while True:
            raw_data, _ = conn.recvfrom(65536)
            dest_mac, src_mac, eth_protocol, eth_data = ethernet_frame(raw_data)  # gather the frame details
            src_port, dst_port = 0, 0
            if eth_protocol == 8:
                s_addr, d_addr, protocol = ipv4_packet(eth_data)
                if protocol == 6:
                    # extracting the TCP source and destination ports
                    src_port, dst_port = tcp_packet(eth_data[34:54])

                elif protocol == 17:
                    # extracting the UDP source and destination ports
                    src_port, dst_port = udp_packet(eth_data[34:38])
                # all the traffic is denied by default
                # all routes in the acl will be allowed
                if validate_with_route_table(s_addr, d_addr, src_port, dst_port):
                    sendpacket(send_sock, eth_data[14:], d_addr)
                    logging.info(f" <ALLOWED> ({s_addr},{d_addr}) > ({src_port}, {dst_port}) >{ PROTOCOLS[protocol]}")
                else:
                    logging.error(f" <FAILED ROUTE> ({s_addr}, {d_addr}) > ({src_port}, {dst_port}) > {PROTOCOLS[protocol]}")
            
    except KeyboardInterrupt:
        print("\nFIREWALL STOPPED")
        exit(1)

if __name__ == "__main__":
    interfaces = get_interfaces()

    print("FIREWALL IS RUNNING ")
    for key in interfaces.items():
        #print(key)
        bind_sockets(key)
