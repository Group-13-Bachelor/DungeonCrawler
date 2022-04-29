import zmq
import sys


class Group(object):

    def __init__(self) -> None:
        pass

    def join():
        pass

    def leave():
        pass

    def hello():
        pass

    def message():
        pass

    def notification():
        pass


def main() -> None:
    if len(sys.argv) < 2:
        print('usage: subscriber <connect_to> [topic topic ...]')
        sys.exit(1)
    print(sys.argv)
    connect_to = sys.argv[1]
    topics = sys.argv[2:]
    ctx = zmq.Context()
    s = ctx.socket(zmq.SUB)
    s.connect(connect_to)

    # manage subscriptions
    if not topics:
        print("Receiving messages on ALL topics...")
        s.setsockopt(zmq.SUBSCRIBE, b'')
    else:
        print("Receiving messages on topics: %s ..." % topics)
        for t in topics:
            s.setsockopt(zmq.SUBSCRIBE, t.encode('utf-8'))
    print
    try:
        while True:
            topic, msg = s.recv_multipart()
            print(
                '   Topic: {}, msg:{}'.format(
                    topic.decode('utf-8'), msg.decode('utf-8')
                )
            )
    except KeyboardInterrupt:
        pass
    print("Done.")


if __name__ == "__main__":
    main()
