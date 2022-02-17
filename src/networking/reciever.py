from __future__ import annotations
from cmath import rect
import socket
import struct
import sys


class Reciever():
    # MSGLEN = 1024                 # Data size
    TTL = struct.pack('b', 2)       # Time to live on network
    TIMEOUT = 5                     # Timer for recieveing data

    def __init__(self, sock=None, group_ip='224.10.11.12', port=5007):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_DGRAM)
        else:
            self.sock = sock

        self.host_ip = self.get_host_ip()
        self.multicast_group = (group_ip, port)

        self.sock.bind((self.host_ip, port))

        self.sock.setsockopt(
            socket.IPPROTO_IP,
            socket.IP_ADD_MEMBERSHIP,
            socket.inet_aton(group_ip) + socket.inet_aton(self.host_ip))

        # self.sock.setblocking(0)    # Set socket to non blocking

    def send(self, message, address=None):
        try:
            if address is None:
                self.sock.sendto(message, self.multicast_group)
            else:
                self.sock.sendto(message, address)
        finally:
            self.sock.close()

    def recieve(self):
        while True:
            print(sys.stderr, '\nwaiting to recieve message')
            data, address = self.sock.recvfrom(1024)
            self.sock.setblocking(0)
            print(sys.stderr, 'recieved %s bytes from %s' % (len(data), address))
            print(sys.stderr, 'sending acknowledgment to', address)
            self.sock.sendto(b'ack', address)
            print('Data: %s' % data)

    def get_host_ip(self) -> str:
        return socket.gethostbyname_ex(socket.gethostname())[2][1]


if __name__ == "__main__":
    reciever = Reciever()
    reciever.recieve()
