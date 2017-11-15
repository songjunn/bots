# -*- coding: utf-8 -*-
import logging
import gevent.monkey
from bots_jks import bots_jks
from bots_ship import bots_ship
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

    def createShipBots(i, addr, port):
        bots = bots_ship.ShipBots(i)
        bots.connectServer(addr, port)
        #bots.schedule(1, bots.test_login)

    def createLeafBots(i, addr, port):
        bots = bots_leaf.LeafBots(i)
        bots.connect(addr, port)

    def createKeystoneBots(i, addr, port):
        bots = bots_keystone.KeystoneBots(i)
        bots.connect(addr, port)

    threads = [
        gevent.spawn(createShipBots, i, "192.168.2.162", "25001") for i in xrange(1024)]
    gevent.joinall(threads)

    while True:
        gevent.sleep(60)

if __name__ == "__main__":
    try:
        start()
    except Exception, ex:
        logging.debug("Ocurred Exception: %s" % str(ex))
        quit()
