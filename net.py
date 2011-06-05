#
# (C) Kristofer Hallin
# kristofer.hallin@gmail.com
#

import os
import sys
import socket
import select

class Listener(object):

    def __init__(self, port, ircsocket, ircchannel):
        self.port = port

    def socket_create(self):
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def socket_bind(self, serversocket):
        serversocket.bind(("", self.port))

    def socket_listen(self, serversocket):
        serversocket.listen(5)
        self.serversocket = serversocket

    def socket_accept(self, serversocket):
        client, address = serversocket.accept()

        return client, address

    def socket_read(self, serversocket):
        return serversocket.recv(1024)

    def create(self):
        serversocket = self.socket_create()
        self.socket_bind(serversocket)
        self.socket_listen(serversocket)

        return serversocket

    def socket_select(self):
        listener = [self.serversocket]
        ready = select.select(listener,[],[])
        client, address = self.socket_accept(self.serversocket)
        data = self.socket_read(client)            
        if data:
            client.close()
            return data
