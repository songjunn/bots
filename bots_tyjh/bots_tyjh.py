# -*- coding: utf-8 -*-
import logging
import gevent.monkey
import protocol
from bots import Bots
from network import socket_client
from google.protobuf import text_format
from message import MessageUser_pb2
from message import MessageTypeDefine_pb2
gevent.monkey.patch_all()

__client_status__ = ['None', 'Connected', 'Online', 'Offline']


class TyjhBots(Bots):
    def __init__(self, id):
        super(TyjhBots, self).__init__(id)
        self._netHandler = socket_client.SocketClient(self.connect_cb, self.shutdown_cb, self.receive_cb)

    def connect_cb(self):
        super(TyjhBots, self).connect_cb()
        #self.schedule(1, self.test_sendData)
        self.requestLogin()

    def shutdown_cb(self):
        super(TyjhBots, self).shutdown_cb()

    def receive_cb(self, data):
        self._recvbuff += data
        proto = protocol.Protocol()
        if proto.unpackage(self._recvbuff) == False:
            return

        self._recvbuff = self._recvbuff[proto.size():len(self._recvbuff)]
        self.handleMessage(proto)

    def handleMessage(self, pack):
        messages = {
            MessageTypeDefine_pb2.MSG_USER_LOGIN_PLAYER: MessageUser_pb2.PlayerLogin(),
        }
        proto = messages.get(pack.type())
        proto.ParseFromString(pack.data())
        logging.debug("Recv message %d size %d: %s", pack.type(),
                      pack.size(), text_format.MessageToString(proto, True, True))

    def sendString(self, data):
        self.sendData(data)
        logging.debug("Send string size %d: %s", len(data), data)

    def sendMsg(self, type, proto):
        message = protocol.Protocol()
        buffer = message.package(type, proto.SerializeToString())
        self.sendData(buffer)
        logging.debug("Send message %d size %d: %s", type, len(buffer),
                      text_format.MessageToString(proto, True, True))

    def test_sendData(self):
        data = "hello python! I'm bots %d" % self._id
        self.sendString(data)

    def requestLogin(self):
        msg = MessageUser_pb2.C2SGuestLogin()
        #msg.name = u"机器人001"
        msg.name = "test100"
        self.sendMsg(MessageTypeDefine_pb2.C2S_GUEST_LOGIN, msg)
