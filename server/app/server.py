# -*- coding: utf-8 -*-
# pylint: disable=

import sys
import logging
from functools import wraps

import Ice

import demo

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s.%(msecs)03d][%(filename)s, %(lineno)d][%(levelname)s]%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


class Calculator(demo.math):

    def add(self, x, y, current=None):
        logging.debug('%s + %s', x, y)
        return x + y

    def substract(self, x, y, current=None):
        logging.debug('%s - %s', x, y)
        return x - y

    def multiply(self, x, y, current=None):
        logging.debug('%s * %s', x, y)
        return x * y

    def divide(self, x, y, current=None):
        logging.debug('%s / %s', x, y)
        return x / y


if __name__ == '__main__':

    with Ice.initialize(sys.argv) as communicator:
        logging.debug('Starting server ...')
        adapter = communicator.createObjectAdapterWithEndpoints(
            'SimpleServerAdapter', 'tcp -h 0.0.0.0 -p 8000')
        object = Calculator()
        adapter.add(object, communicator.stringToIdentity('SimpleServer'))
        adapter.activate()

        logging.debug('Waiting for connection ...')
        communicator.waitForShutdown()
