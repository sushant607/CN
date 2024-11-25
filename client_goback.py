import socket
import time

# Configuration for the client
server_details = ('localhost', 8080)
win_size = 4
current_base = 0
sequence_number = 0
response_timeout = 2

# Initialize UDP socket
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_client_socket.settimeout(response_timeout)

def transmit_packet(seq):
    packet = str(seq)
    udp_client_socket.sendto(packet.encode(), server_details)
    print(f"Packet {seq} has been sent")

while current_base < 10:  # SendQ a total of 10 packets for this example
    while sequence_number < current_base + win_size and sequence_number < 10:
        transmit_packet(sequence_number)
        sequence_number += 1

    try:
        while current_base < sequence_number:
            acknowledgment, _ = udp_client_socket.recvfrom(1024)
            ack_seq = int(acknowledgment.decode().split()[1])
            print(f"Received acknowledgment: {acknowledgment.decode()}")
            if ack_seq >= current_base:
                current_base = ack_seq + 1
    except socket.timeout:
        print("Timeout detected! Re-sending packets starting from current base...")
        sequence_number = current_base

udp_client_socket.close()
