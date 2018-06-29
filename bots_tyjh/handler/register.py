# -*- coding: utf-8 -*-

from message import MessageTypeDefine_pb2
from message import MessageUser_pb2
from message import MessagePlayer_pb2

from handler import userHandler


protocols = {
    MessageTypeDefine_pb2.S2C_USER_LOGIN: MessageUser_pb2.S2CUserLogin(),
}

handlers = {
	MessageTypeDefine_pb2.S2C_USER_LOGIN: userHandler.handleS2CUserLogin,
}