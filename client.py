import socket
import time

# Client settings
server_address = ('localhost', 8080)
window_size = 4
base = 0
next_seq = 0
timeout = 2

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(timeout)

def send_packet(seq_num):
    message = str(seq_num)
    client_socket.sendto(message.encode(), server_address)
    print(f"Sent packet {seq_num}")

while base < 10:  # Sending 10 packets for demonstration
    while next_seq < base + window_size and next_seq < 10:
        send_packet(next_seq)
        next_seq += 1

    try:
        while base < next_seq:
            ack, _ = client_socket.recvfrom(1024)
            ack_num = int(ack.decode().split()[1])
            print(f"Received {ack.decode()}")
            if ack_num >= base:
                base = ack_num + 1

    except socket.timeout:
        print("Timeout! Resending from base...")
        next_seq = base

client_socket.close()
