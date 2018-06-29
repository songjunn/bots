# -*- coding: utf-8 -*-

import logging
from message import MessageTypeDefine_pb2
from message import MessagePlayer_pb2

def handleS2CUserLogin(data):
	msg = MessageUser_pb2.C2SPlayerCreate()
	msg.name = "player001"
	msg.gender = 1
	msg.vocation = 3