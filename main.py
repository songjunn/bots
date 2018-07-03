# -*- coding: utf-8 -*-
import logging
import gevent.monkey
from botsMgr import BotsMgr
from bots_tyjh import bots_tyjh
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
        BotsMgr().addBotsByIdx(i, bots)

    threads = [
        gevent.spawn(createTyjhBots, i, "192.168.0.210", "15001") for i in xrange(1)]
    gevent.joinall(threads)

    while True:
        gevent.sleep(60)

if __name__ == "__main__":
    try:
        start()
    except Exception as ex:
        logging.debug("Ocurred Exception: %s" % str(ex))
        quit()
