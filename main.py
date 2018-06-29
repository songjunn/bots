# -*- coding: utf-8 -*-
import logging
import gevent.monkey
from bots_tyjh import bots_tyjh
#from bots_ship import bots_ship
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

    def createTyjhBots(i, addr, port):
        bots = bots_tyjh.TyjhBots(i)
        bots.connect(addr, port)

    #def createShipBots(i, addr, port):
    #    bots = bots_ship.ShipBots(i)
    #    bots.connectServer(addr, port)
    #    bots.schedule(1, bots.test_login)

    threads = [
        gevent.spawn(createTyjhBots, i, "123.207.143.200", "15001") for i in xrange(1)]
    gevent.joinall(threads)

    while True:
        gevent.sleep(60)

if __name__ == "__main__":
    try:
        start()
    except Exception as ex:
        logging.debug("Ocurred Exception: %s" % str(ex))
        quit()
