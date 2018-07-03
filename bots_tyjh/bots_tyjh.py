# -*- coding: utf-8 -*-
import sys
path = __file__[:__file__.rfind("\\")]
sys.path.append(path)

import logging
import gevent.monkey
import protocol
from bots import Bots
from google.protobuf import text_format
from handler import register
from message import MessageUser_pb2
from message import MessageTypeDefine_pb2
gevent.monkey.patch_all()

__client_status__ = ['None', 'Connected', 'Online', 'Offline']


class TyjhBots(Bots):
    def __init__(self, id):
        super(TyjhBots, self).__init__(id)
        self.uid_ = 0
        self.players = {}

    def connect_cb(self):
        super(TyjhBots, self).connect_cb()
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
        proto = register.protocols.get(pack.type())
        proto.ParseFromString(pack.data())
        logging.debug("Recv message %d size %d: %s", pack.type(),
                      pack.size(), text_format.MessageToString(proto, True, True))
        register.handlers.get(pack.type())(self, proto)

    def sendMsg(self, type, proto):
        message = protocol.Protocol()
        buffer = message.package(type, proto.SerializeToString())
        self.sendData(buffer)
        logging.debug("Send message %d size %d: %s", type, len(buffer),
                      text_format.MessageToString(proto, True, True))

    def requestLogin(self):
        msg = MessageUser_pb2.C2SGuestLogin()
        #msg.name = u"机器人001"
        msg.name = "bots-" + str(self._index)
        self.sendMsg(MessageTypeDefine_pb2.C2S_GUEST_LOGIN, msg)
