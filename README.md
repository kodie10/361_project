People will request Data from my microservice using ZeroMQ.
They will set up the socket send the request formatted as a string.
then they will wait for the response that will be JSON formatted string.
example,

context = zmq.Context()
#  Socket to talk to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
socket.send_string(whatever they are sending)
socket.recv_string(requested data)


![image](https://user-images.githubusercontent.com/86174843/218130603-c2f2d22c-0af3-45a8-900e-af6a219ad2b3.png)
