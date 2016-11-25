# -*- coding: utf-8 -*-
import logging
import gevent.monkey
import protocol
from bots import Bots
from network import socket_client
from network import websocket_client
from google.protobuf import text_format
from message import MessageUser_pb2
from message import MessageTypeDefine_pb2
gevent.monkey.patch_all()

__client_status__ = ['None', 'Connected', 'Online', 'Offline']


class TankBots(Bots):
    def __init__(self, id):
        super(TankBots, self).__init__(id)
        #self._netHandler = websocket_client.WebSocketClient(self.connect_cb, self.shutdown_cb, self.receive_cb)
        self._netHandler = socket_client.SocketClient(self.connect_cb, self.shutdown_cb, self.receive_cb)

    def connect_cb(self):
        super(TankBots, self).connect_cb()
        self.requestLogin()
        #self.schedule(10, self.test_sendData)
        #self.test_sendData()

    def shutdown_cb(self):
        super(TankBots, self).shutdown_cb()

    def receive_cb(self, data):
        self._recvbuff += data
        proto = protocol.Protocol()
        if proto.unpackage(self._recvbuff) == False:
            return

        self._recvbuff = self._recvbuff[proto.size():len(self._recvbuff)]
        self.handleMessage(proto)

    def handleMessage(self, pack):
        #messages = {
        #    MessageTypeDefine_pb2.MSG_USER_LOGIN_PLAYER: MessageUser_pb2.PlayerLogin(),
        #}
        #proto = messages.get(pack.type())
        #proto.ParseFromString(pack.data())
        #logging.debug("Recv message %d size %d: %s", pack.type(),
        #              pack.size(), text_format.MessageToString(proto, True, True))
        pass

    def sendString(self, data):
        message = protocol.Protocol()
        buffer = message.package(0, data)
        self.sendData(buffer)
        #logging.debug("Send string size %d: {%s}", len(buffer), data)
        logging.debug("Send string size %d", len(buffer))

    def sendMsg(self, type, proto):
        message = protocol.Protocol()
        buffer = message.package(type, proto.SerializeToString())
        self.sendData(buffer)
        logging.debug("Send message %d size %d: {%s}", type, len(buffer),
                      text_format.MessageToString(proto, True, True))

    def test_sendData(self):
        data = "afhajfdasfkhsdjfhksjafhkshfshdfksadhfjshdiueeeeeeieuhfskdhaifdshfjhsdjfhjsdfhjshfksdhfkdsjhfkshdfkshfkdshfkdshfksjfsjfhsdfjsdkfhiewekjshfiuwhejdshfjhsdkjjjjjjjdhfskjdfhueiwrhjsdfuichvbehwiuafhajfdasfkhsdjfhksjafhkshfshdfksadhfjshdiueeeeeeieuhfskdhaifdshfjhsdjfhjsdfhjshfksdhfkdsjhfkshdfkshfkdshfkdshfksjfsjfhsdfjsdkfhiewekjshfiuwhejdshfjhsdkjjjjjjjdhafhajfdasfkhsdjfhksjafhkshfshdfksadhfjshdiueeeeeeieuhfskdhaifdshfjhsdjfhjsdfhjshfksdhfkdsjhfkshdfkshfkdshfkdshfksjfsjfhsdfjsdkfhiewekjshfiuwhejdshfjhsdkjjjjjjjdhfskjdfhueiwrhjsdfuichvbehwiurhsdabcvhadfhuicgvwghefbasdjhiviafhajfdasfkhsdjfhksjafhkshfshdfksadhfjshdiueeeeeeieuhfskdhaifdshfjhsdjfhjsdfhjshfksdhfkdsjhfkshdfkshfkdshfkdshfksjfsjfhsdfjsdkfhiewekjshfiuwhejdshfjhsdkjjjjjjjdhfskjdfhueiwrhjsdfuichvbehwiurhsdabcvhadfhuicgvwghefbasdjhiviafhajfdasfkhsdjfhksjafhkshfshdfksadhfjshdiueeeeeeieuhfskdhaifdshfjhsdjfhjsdfhjshfksdhfkdsjhfkshdfkshfkdshfkdshfksjfsjfhsdfjsdkfhiewekjshfiuwhejdshfjhsdkjjjjjjjdhfskjdfhueiwrhjsdfuichvbehwiurhsdabcvhadfhuicgvwghefbasdjhiviafhajfdasfkhsdjfhksjafhkshfshdfksadhfjshdiueeeeeeieuhfskdhaifdshfjhsdjfhjsdfhjshfksdhfkdsjhfkshdfkshfkdshfkdshfksjfsjfhsdfjsdkfhiewekjshfiuwhejdshfjhsdkjjjjjjjdhfskjdfhueiwrhjsdfuichvbehwiurhsdabcvhadfhuicgvwghefbasdjhiviafhajfdasfkhsdjfhksjafhkshfshdfksadhfjshdiueeeeeeieuhfskdhaifdshfjhsdjfhjsdfhjshfksdhfkdsjhfkshdfkshfkdshfkdshfksjfsjfhsdfjsdkfhiewekjshfiuwhejdshfjhsdkjjjjjjjdhfskjdfhueiwrhjsdfuichvbehwiurhsdabcvhadfhuicgvwghefbasdjhiviafhajfdasfkhsdjfhksjafhkshfshdfksadhfjshdiueeeeeeieuhfskdhaifdshfjhsdjfhjsdfhjshfksdhfkdsjhfkshdfkshfkdshfkdshfksjfsjfhsdfjsdkfhiewekjshfiuwhejdshfjhsdkjjjjjjjdhfskjdfhueiwrhjsdfuichvbehwiurhsdabcvhadfhuicgvwghefbasdjhiviafhajfdasfkhsdjfhksjafhkshfshdfksadhfjshdiueeeeeeieuhfskdhaifdshfjhsdjfhjsdfhjshfksdhfkdsjhfkshdfkshfkdshfkdshfksjfsjfhsdfjsdkfhiewekjshfiuwhejdshfjhsdkjjjjjjjdhfskjdfhueiwrhjsdfuichvbehwiurhsdabcvhadfhuicgvwghefbasdjhiviafhajfdasfkhsdjfhksjafhkshfshdfksadhfjshdiueeeeeeieuhfskdhaifdshfjhsdjfhjsdfhjshfksdhfkdsjhfkshdfkshfkdshfkdshfksjfsjfhsdfjsdkfhiewekjshfiuwhejdshfjhsdkjjjjjjjdhfskjdfhueiwrhjsdfuichvbehwiurhsdabcvhadfhuicgvwghefbasdjhivifskjdfhueiwrhjsdfuichvbehwiurhsdabcvhadfhuicgvwghefbasdjhivirhsdabcvhadfhuicgvwghefbasdjhivi"
        self.sendString(data)

    def requestLogin(self):
        #msg = MessageUser_pb2.DceGuestLogin()
        #msg.guest = "bots_001"
        #msg.world = 1
        #self.sendMsg(MessageTypeDefine_pb2.DCE_GUEST_LOGIN, msg)
        data = "gl" + ",1" + ",guest" + str(self._id)
        self.sendString(data)
