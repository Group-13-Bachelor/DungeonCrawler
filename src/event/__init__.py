import time
import zmq

context = zmq.Context()
reciever = context.socket(zmq.PULL)
reciever.connect("tcp://localhost:5557")

subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://localhost:5556")
subscriber.setsockopt(zmq.SUBSCRIBE, b'10001')

rc = zmq.connect()

while True:
    while True:
        try:
            msg = reciever.recv(zmq.DONTWAIT)
        except zmq.Again:
            break

    while True:
        try:
            msg = subscriber.recv(zmq.DONTWAIT)
        except zmq.Again:
            break

    time.sleep(0.001)
