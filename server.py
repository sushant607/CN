import socket
import random

# Server settings
server_address = ('localhost', 8080)
window_size = 4
expected_seq = 0

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(server_address)
print(f"Go-Back-N Server running on {server_address}")

while True:
    try:
        data, client_address = server_socket.recvfrom(1024)
        seq_num = int(data.decode())

        # Simulate packet loss (10% chance)
        if random.random() < 0.1:
            print(f"Packet with sequence number {seq_num} lost")
            continue

        if seq_num == expected_seq:
            print(f"Received packet {seq_num}, sending ACK {seq_num}")
            ack = f"ACK {seq_num}"
            server_socket.sendto(ack.encode(), client_address)
            expected_seq += 1
        else:
            print(f"Packet {seq_num} out of order, expecting {expected_seq}")
            ack = f"ACK {expected_seq - 1}"
            server_socket.sendto(ack.encode(), client_address)

    except KeyboardInterrupt:
        print("Server shutting down.")
        break

server_socket.close()
