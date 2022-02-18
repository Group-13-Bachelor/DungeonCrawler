# from __future__ import annotations
import socket
import struct
import asyncio


class MulticastRecieverProtocol:
    def __init__(self, on_con_lost):
        self.on_con_lost = on_con_lost
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        """Is called when data is recieved on the socket"""
        message = data.decode()
        print('Received %r from %s' % (message, addr))
        print('Send %r to %s' % (b'ack', addr))
        self.transport.sendto('ack'.encode(), addr)

    def connection_lost(self, exc):
        """Is called when the socket loses connection"""
        # The socket has been closed
        self.on_con_lost.set_result(True)


class Reciever():
    # MSGLEN = 1024                 # Data size
    TTL = struct.pack('b', 2)       # Time to live on network
    TIMEOUT = 5                     # Timer for recieveing data

    def __init__(self, sock=None, group_ip='224.10.11.12', port=5007):
        # Socket config
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_DGRAM)
        else:
            self.sock = sock

        self.host_ip = self.get_host_ip()           # lan ip address
        self.multicast_group = (group_ip, port)     # multicast group ip and port

        self.sock.bind((self.host_ip, port))

        self.sock.setsockopt(
            socket.IPPROTO_IP,
            socket.IP_ADD_MEMBERSHIP,
            socket.inet_aton(group_ip) + socket.inet_aton(self.host_ip))

    async def start_server(self):
        self.loop = asyncio.get_running_loop()
        self.transport, self.protocol = await self.loop.create_datagram_endpoint(
            lambda: MulticastRecieverProtocol(self.loop.create_future()),
            sock=self.sock
        )
        print("Starting server...\n")

    def stop_server(self):
        self.transport.close()
        self.sock.close()

    def get_host_ip(self) -> str:
        """Gets the lan ip address of the host"""
        return socket.gethostbyname_ex(socket.gethostname())[2][1]


if __name__ == "__main__":
    reciever = Reciever()
    asyncio.run(reciever.start_server())
