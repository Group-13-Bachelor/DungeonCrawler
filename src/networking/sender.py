import socket
import struct
import sys


class Sender():
    TTL = struct.pack('b', 2)       # Time to live on network
    TIMEOUT = 3                   # Timer for recieveing data in seconds

    def __init__(self, sock=None, group_ip='224.10.11.12', port=5007):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_DGRAM)
        else:
            self.sock = sock

        self.multicast_group = (group_ip, port)

        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, self.TTL)

        self.sock.settimeout(self.TIMEOUT)    # Set timout timer

    def send(self, message):
        try:
            self.sock.sendto(message, self.multicast_group)
            self.ack()
        finally:
            self.sock.close()

    def ack(self):
        data = ''
        while data != b'ack':
            try:
                data, server = self.sock.recvfrom(16)
            except(socket.timeout):
                print(sys.stderr, 'timed out, no more responses')
                break
            else:
                print(sys.stderr, 'recieved "%s" from %s' % (data, server))


if __name__ == '__main__':
    # from networking.reciever import Reciever
    # reciever = Reciever()
    # reciever.recieve()
    sender = Sender()
    sender.send(b"Hello, world!")
