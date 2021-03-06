import socket, asyncore, asynchat, json
from pywsserver.websocket import WebSocketConnection

class DummyServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accepted(self, sock, addr):
        print('Incoming connection from %s' % repr(addr))
        handler = DummyConnection(sock, addr)

class DummyConnection(WebSocketConnection):
    def handle_binary_message(self, data):
        self.send_binary_message(data)
    
    def handle_utf8_message(self, data):
        self.send_utf8_message(data)
