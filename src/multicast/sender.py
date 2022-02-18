import asyncio
import socket
import struct


class SenderProtocol:
    def __init__(self, message, on_con_lost, multicast_grp):
        self.message = message.encode()
        self.on_con_lost = on_con_lost
        self.multicast_grp = multicast_grp
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        print('Send:', self.message)
        self.transport.sendto(self.message, self.multicast_grp)

    def datagram_received(self, data, addr):
        print("Received:", data.decode())
        print("Close the socket")
        self.transport.close()

    def error_received(self, exc):
        print('Error received:', exc)

    def connection_lost(self, exc):
        print("Connection closed")
        self.on_con_lost.set_result(True)


class Sender():
    TTL = struct.pack('b', 2)       # Time to live on network
    TIMEOUT = 3                   # Timer for recieveing data in seconds

    def __init__(self, sock=None, group_ip='224.10.11.12', port=5007):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_DGRAM)
        else:
            self.sock = sock

        self.sock.setblocking(False)
        self.sock.settimeout(self.TIMEOUT)    # Set timout timer
        self.multicast_group = (group_ip, port)

        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, self.TTL)

    async def send(self, message):
        loop = asyncio.get_running_loop()
        on_con_lost = loop.create_future()
        transport, protocol = await loop.create_datagram_endpoint(
            lambda: SenderProtocol(message, on_con_lost, self.multicast_group),
            sock=self.sock)
        try:
            await on_con_lost
        finally:
            transport.close()


if __name__ == '__main__':
    sender = Sender()
    asyncio.run(sender.send("Hello, world!"))
