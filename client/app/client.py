# -*- coding: utf-8 -*-
# pylint: disable=

import time
from random import randint
import logging
import sys
import Ice

import demo


if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s.%(msecs)03d][%(filename)s, %(lineno)d][%(levelname)s]%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    with Ice.initialize(sys.argv) as communicator:
        # server is a service name when using docker
        base = communicator.stringToProxy("SimpleServer:tcp -h server -p 8000")
        server = demo.mathPrx.checkedCast(base)
        if not server:
            raise RuntimeError("Invalid proxy")

        while(True):
            logging.debug(server.add(randint(100, 200), randint(100, 200)))
            time.sleep(1)

