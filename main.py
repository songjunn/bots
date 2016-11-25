# -*- coding: utf-8 -*-
import logging
import gevent.monkey
from bots_jks import bots_jks
from bots_tank import bots_tank
from bots_leaf import bots_leaf
from bots_keystone import bots_keystone
gevent.monkey.patch_all()


def init_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(module)s-L%(lineno)d-%(levelname)s: %(message)s')
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    logging.info(
        "Set logging level: %s", logging.getLevelName(logger.getEffectiveLevel()))


def start():
    init_logging()

    def createJksBots(i, addr, port):
        bots = bots_jks.JksBots(i)
        bots.connect(addr, port)

    def createTankBots(i, addr, port):
        bots = bots_tank.TankBots(i)
        bots.connect(addr, port)

    def createLeafBots(i, addr, port):
        bots = bots_leaf.LeafBots(i)
        bots.connect(addr, port)

    def createKeystoneBots(i, addr, port):
        bots = bots_keystone.KeystoneBots(i)
        bots.connect(addr, port)

    threads = [
        gevent.spawn(createKeystoneBots, i, "192.168.5.7", "20000") for i in xrange(1)]
    gevent.joinall(threads)

    while True:
        gevent.sleep(60)

if __name__ == "__main__":
    try:
        start()
    except Exception, ex:
        logging.debug("Ocurred Exception: %s" % str(ex))
        quit()
