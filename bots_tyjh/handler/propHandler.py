# -*- coding: utf-8 -*-

import logging
from botsMgr import BotsMgr
from message import MessageTypeDefine_pb2
from message import MessageProp_pb2

def handleS2CPropList(bots, data):
	for prop in data.proplist:
		bots.proplist.append(prop)
	logging.debug('Recv %d props' % (len(data.proplist)))
	if len(data.proplist) < 1:
		buyProp(bots)

def buyProp(bots):
	msg = MessageProp_pb2.C2SPropBuy()
	msg.index = 1
	msg.count = 2
	bots.sendMsg(MessageTypeDefine_pb2.C2S_PROP_BUY, msg)
