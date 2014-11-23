"""
PUSH/PULL example
Implements a PUSH socket, which sends messages entered by the user. 'pull.py'
should be started before 'push.py' since 'pull.py' binds the socket.
"""

import zmq

# Setup PUSH socket
context = zmq.Context()
zmq_socket = context.socket(zmq.PUSH)
zmq_socket.connect("tcp://127.0.0.1:5557")

# Message loop
print('Enter message to send.')
while True:
    message = raw_input("> ")
    zmq_socket.send_json({'message': message})
