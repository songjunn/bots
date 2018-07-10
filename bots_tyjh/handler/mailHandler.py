# -*- coding: utf-8 -*-

import logging
from botsMgr import BotsMgr
from message import MessageTypeDefine_pb2
from message import MessageMail_pb2

def handleS2CMailList(bots, data):
	for mail in data.maillist:
		bots.maillist.append(mail)
	logging.debug('Recv %d mails' % (len(data.maillist)))
	if len(data.maillist) < 1:
		sendMail(bots)

def sendMail(bots):
	msg = MessageMail_pb2.C2SMailSend()
	msg.fromid = bots.uid
	msg.toid = bots.uid
	msg.title = 'test'
	msg.content = 'hello world'
	msg.expiry = 1
	bots.sendMsg(MessageTypeDefine_pb2.C2S_MAIL_SEND, msg)
