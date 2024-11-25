import socket
import time

# Client configuration
server_details = ('localhost', 8081)
win_size = 4
packet_tracker = {}
timeout_interval = 2

# Set up a UDP client socket
udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_client_socket.settimeout(timeout_interval)

def transmit_packet(sequence_num):
    packet_data = str(sequence_num)
    udp_client_socket.sendto(packet_data.encode(), server_details)
    packet_tracker[sequence_num] = time.time()
    print(f"Packet {sequence_num} sent")

sequence_number = 0
while sequence_number < 10:  # Example: Send a total of 10 packets
    while sequence_number < sequence_number + win_size and sequence_number < 10:
        transmit_packet(sequence_number)
        sequence_number += 1

    try:
        while packet_tracker:
            acknowledgment, _ = udp_client_socket.recvfrom(1024)
            ack_sequence = int(acknowledgment.decode().split()[1])
            print(f"Received acknowledgment: {acknowledgment.decode()}")

            if ack_sequence in packet_tracker:
                del packet_tracker[ack_sequence]
    except socket.timeout:
        print("Timeout detected! Resending all unacknowledged packets...")
        for seq_num in list(packet_tracker):
            if time.time() - packet_tracker[seq_num] >= timeout_interval:
                transmit_packet(seq_num)

udp_client_socket.close()
