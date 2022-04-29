import ipaddress
import socket

MULTICAST_GRP = '255.25.25.25'


def get_host_ip() -> str:
    return socket.gethostbyname_ex(socket.gethostname())[2][1]


class Beacon(object):
    def __init__(self) -> None:
        self.udpsock = socket.socket(socket.AF_INET, socket.SOCK.DGRAM, socket.IPPROTO_UDP)
        self.address = None

    def __del__(self):
        '''Close socket if object is deleted'''
        if self.udpsock:
            self.udpsock.close()

    def create_udp_socket(self):
        self.address = ipaddress.IPv4Address(get_host_ip)
        self.multicast_grp = ipaddress.IPv4Address(MULTICAST_GRP)

        self.udpsock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.udpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.udpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.udpsock.setsockopt(socket.IPPROTO_IP, socket.socket.IP_MULTICAST_TTL, 2)

        self.udpsock.setsockopt(socket.SOL_IP, socket.IP_ADD_MEMBERSHIP,
            socket.inet_aton(self.multicast_grp) +
                socket.inet_aton(self.address))
        self.udpsock.bind(('', self.port_nbr))


import itertools
import sys
import time
import zmq


def main() -> None:
    if len(sys.argv) != 2:
        print('usage: publisher <bind-to>')
        sys.exit(1)

    bind_to = sys.argv[1]

    all_topics = [
        b'sports.general',
        b'sports.football',
        b'sports.basketball',
        b'stocks.general',
        b'stocks.GOOG',
        b'stocks.AAPL',
        b'weather',
    ]

    ctx = zmq.Context()
    s = ctx.socket(zmq.PUB)
    s.bind(bind_to)

    print("Starting broadcast on topics:")
    print(f"   {all_topics}")
    print("Hit Ctrl-C to stop broadcasting.")
    print("Waiting so subscriber sockets can connect...")
    print("")
    time.sleep(1.0)

    msg_counter = itertools.count()
    try:
        for topic in itertools.cycle(all_topics):
            msg_body = str(next(msg_counter))
            print(f"   Topic: {topic.decode('utf8')}, msg:{msg_body}")
            s.send_multipart([topic, msg_body.encode("utf8")])
            # short wait so we don't hog the cpu
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass

    print("Waiting for message queues to flush...")
    time.sleep(0.5)
    print("Done.")


if __name__ == "__main__":
    main()