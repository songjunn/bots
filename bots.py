# -*- coding: utf-8 -*-
import logging

from network.socket_client import SocketClient as NetClient
import gevent.monkey
gevent.monkey.patch_all()


class Bots(NetClient):
    def __init__(self, index):
        super(Bots, self).__init__()
        self._index = index

    def connect_cb(self):
        super(Bots, self).connect_cb()
        logging.info("Bots %d connect success...", self._index)

    def shutdown_cb(self):
        super(Bots, self).connect_cb()
        logging.info("Bots %d shutdown...", self._index)

    def receive_cb(self, data):
        super(Bots, self).receive_cb()

    def schedule(self, interval, func):
        def looper():
            while True:
                func()
                gevent.sleep(interval)
        gevent.spawn(looper)
