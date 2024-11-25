import socket
import random

# Server configuration
server_details = ('localhost', 8080)
win_size = 4
next_expected_seq = 0

# Initialize the UDP server socket
udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_socket.bind(server_details)
print(f"Go-Back-N protocol server started on {server_details}")

while True:
    try:
        data, client_info = udp_server_socket.recvfrom(1024)
        received_seq = int(data.decode())

        # Introduce packet loss simulation with a 10% probability
        if random.random() < 0.1:
            print(f"Simulating loss of packet with sequence number {received_seq}")
            continue

        if received_seq == next_expected_seq:
            print(f"Packet {received_seq} arrived, sending acknowledgment for {received_seq}")
            ack_message = f"ACK {received_seq}"
            udp_server_socket.sendto(ack_message.encode(), client_info)
            next_expected_seq += 1
        else:
            print(f"Packet {received_seq} out of order, waiting for {next_expected_seq}")
            ack_message = f"ACK {next_expected_seq - 1}"
            udp_server_socket.sendto(ack_message.encode(), client_info)
    except KeyboardInterrupt:
        print("Shutting down the server gracefully.")
        break

udp_server_socket.close()
