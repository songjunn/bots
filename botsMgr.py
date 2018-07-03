# -*- coding: utf-8 -*-
import logging
from utils.singleton import Singleton

class BotsMgr(Singleton):
	def __init__(self):
		super(BotsMgr, self).__init__()
		self.botsIdx = {}
		self.botsUid = {}

	def addBotsByIdx(self, idx, bots):
		self.botsIdx[idx] = bots

	def delBotsByIdx(self, idx):
		del self.botsIdx[idx]

	def getBotsByIdx(self, idx):
		return self.botsIdx[idx]

	def addBotsByUid(self, uid, bots):
		self.botsUid[uid] = bots

	def delBotsByUid(self, uid):
		del self.botsUid[uid]

	def getBotsByUid(self, uid):
		return self.botsUid[uid]
