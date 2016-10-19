# -*- coding: utf-8 -*-
import logging
import gevent.monkey
from gevent.queue import Queue
from gevent.socket import socket
gevent.monkey.patch_all()


class SocketClient(object):
    def __init__(self, connect_cb = None, shutdown_cb = None, receive_cb = None):
        self._sockfd = None
        self._recvbuff = ""
        self._sendqueue = Queue()
        self._work = False
        self._cbConnect = connect_cb
        self._cbShutdown = shutdown_cb
        self._cbReceive = receive_cb

    def connect(self, host, port):
        self._work = True
        self._sockfd = gevent.socket.socket()
        self._sockfd.connect((host, port))
        self._cbConnect()
        gevent.spawn(self._writer)
        gevent.spawn(self._reader)

    def shutdown(self):
        self._work = False
        self._sockfd.close()
        self._cbShutdown()

    def sendData(self, data):
        self._sendqueue.put(data)

    def _reader(self):
        while self._work:
            data = self._sockfd.recv(1024)
            if not data:
                self.shutdown()
            else:
                logging.debug("Recv size %d", len(data))
                self._cbReceive(data)
            # gevent.sleep(1)

    def _writer(self):
        while self._work:
            if not self._sendqueue.empty():
                data = self._sendqueue.get()
                self._sockfd.sendall(data)
                logging.debug("Send size %d", len(data))
            gevent.sleep(1)
