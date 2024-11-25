import socket
import random

# Server configuration
server_details = ('localhost', 8081)
win_size = 4
received_packets = {}

# Initialize a UDP server socket
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.bind(server_details)
print(f"Selective Repeat Protocol Server started on {server_details}")

while True:
    try:
        data, client_info = udp_server_socket.recvfrom(1024)
        packet_seq_num = int(data.decode())

        # Simulating random packet loss with a 10% probability
        if random.random() < 0.1:
            print(f"Simulated loss for packet with sequence number {packet_seq_num}")
            continue

        print(f"Packet {packet_seq_num} received successfully")
        received_packets[packet_seq_num] = True

        acknowledgment_message = f"ACK {packet_seq_num}"
        udp_server_socket.sendto(acknowledgment_message.encode(), client_info)
    except KeyboardInterrupt:
        print("Gracefully shutting down the server.")
        break

udp_server_socket.close()
