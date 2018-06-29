# -*- coding: utf-8 -*-
import logging
import gevent.monkey
from gevent.queue import Queue
from gevent.socket import socket
gevent.monkey.patch_all()

__client_status__ = ['None', 'Connected', 'Online', 'Offline']

class SocketClient(object):
    def __init__(self):
        self._work = False
        self._sockfd = None
        self._recvbuff = ""
        self._sendqueue = Queue()
        self._status = __client_status__[0]

    def connect(self, host, port):
        self._work = True
        self._sockfd = gevent.socket.socket()
        self._sockfd.connect((host, port))
        self.connect_cb()
        gevent.spawn(self._writer)
        gevent.spawn(self._reader)

    def shutdown(self):
        self._work = False
        self._sockfd.close()
        self.shutdown_cb()

    def sendData(self, data):
        self._sendqueue.put(data)

    def connect_cb(self):
        self._status = __client_status__[1]

    def shutdown_cb(self):
        self._status = __client_status__[3]

    def receive_cb(self, data):
        pass

    def _reader(self):
        while self._work:
            data = self._sockfd.recv(1024)
            if not data:
                self.shutdown()
            else:
                logging.debug("Recv size %d", len(data))
                self.receive_cb(data)
            # gevent.sleep(1)

    def _writer(self):
        while self._work:
            if not self._sendqueue.empty():
                data = self._sendqueue.get()
                self._sockfd.sendall(data)
                logging.debug("Send size %d", len(data))
            gevent.sleep(1)
