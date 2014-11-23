"""
PUSH/PULL example
Implements a PULL socket, which receives and displays messages entered by the
user. 'pull.py' should be started before 'push.py' since 'pull.py' binds the
socket.
"""

import zmq

# Setup PULL socket
context = zmq.Context()
zmq_socket = context.socket(zmq.PULL)
zmq_socket.bind("tcp://127.0.0.1:5557")

# Message loop
while True:
    payload = zmq_socket.recv_json()
    print('Message received: {0}'.format(payload['message']))
