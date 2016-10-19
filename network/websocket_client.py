# -*- coding: utf-8 -*-
import logging
import websocket
import gevent.monkey
gevent.monkey.patch_all()


class WebSocketClient(object):
    def __init__(self, connect_cb = None, shutdown_cb = None, receive_cb = None):
        self._wsInstance = None
        self._recvbuff = ""
        self._cbConnect = connect_cb
        self._cbShutdown = shutdown_cb
        self._cbReceive = receive_cb

    def connect(self, host, port):
        websocket.enableTrace(True)
        self._wsInstance = websocket.WebSocketApp("ws://" + host + ":" + port,
                                                 on_open=self._onOpen,
                                                 on_message=self._onMessage,
                                                 on_error=self._onError,
                                                 on_close=self._onClose)
        gevent.spawn(self._wsInstance.run_forever)

    def shutdown(self):
        self._wsInstance.close()
        self._cbShutdown()

    def sendData(self, data):
        self._wsInstance.send(data)

    def _onOpen(self, ws):
        self._cbConnect()

    def _onClose(self, ws):
        self._cbShutdown()

    def _onMessage(self, ws, message):
        self._cbReceive(message)

    def _onError(self, ws, error):
        print error
