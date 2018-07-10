# -*- coding: utf-8 -*-

from message import MessageTypeDefine_pb2
from message import MessageUser_pb2
from message import MessagePlayer_pb2
from message import MessageProp_pb2
from message import MessageMail_pb2

from handler import userHandler
from handler import propHandler
from handler import mailHandler


protocols = {
    MessageTypeDefine_pb2.S2C_USER_LOGIN: MessageUser_pb2.S2CUserLogin(),
    MessageTypeDefine_pb2.S2C_PROP_LIST: MessageProp_pb2.S2CPropList(),
    MessageTypeDefine_pb2.S2C_MAIL_LIST: MessageMail_pb2.S2CMailList(),
}

handlers = {
	MessageTypeDefine_pb2.S2C_USER_LOGIN: userHandler.handleS2CUserLogin,
	MessageTypeDefine_pb2.S2C_PROP_LIST: propHandler.handleS2CPropList,
	MessageTypeDefine_pb2.S2C_MAIL_LIST: mailHandler.handleS2CMailList,
}