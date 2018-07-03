# -*- coding: utf-8 -*-

import logging
from botsMgr import BotsMgr
from message import MessageTypeDefine_pb2
from message import MessagePlayer_pb2

def handleS2CUserLogin(bots, data):
	bots.uid = data.uid
	BotsMgr().addBotsByUid(bots.uid, bots)

	if len(data.playerlist) <= 0 :
		msg = MessagePlayer_pb2.C2SPlayerCreate()
		msg.name = "player001"
		msg.gender = 1
		msg.vocation = 3
		bots.sendMsg(MessageTypeDefine_pb2.C2S_PLAYER_CREATE, msg)
	else:
		msg = MessagePlayer_pb2.C2SPlayerLogin()
		msg.pid = data.playerlist[0].pid
		bots.sendMsg(MessageTypeDefine_pb2.C2S_PLAYER_LOGIN, msg)
	
