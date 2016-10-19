# -*- coding: utf-8 -*-
import logging
import gevent.monkey
gevent.monkey.patch_all()

__client_status__ = ['None', 'Connected', 'Online', 'Offline']


class Bots(object):
    def __init__(self, id):
        self._id = id
        self._status = __client_status__[0]
        self._netHandler = None

    def connect(self, host, port):
        self._netHandler.connect(host, port)

    def shutdown(self):
        self._netHandler.shutdown()

    def sendData(self, data):
        self._netHandler.sendData(data)

    def connect_cb(self):
        self._status = __client_status__[1]
        logging.info("Bots %d connect success...", self._id)

    def shutdown_cb(self):
        self._status = __client_status__[3]
        logging.info("Bots %d shutdown...", self._id)

    def receive_cb(self, data):
        pass

    def schedule(self, interval, func):
        def looper():
            while True:
                func()
                gevent.sleep(interval)
        gevent.spawn(looper)
