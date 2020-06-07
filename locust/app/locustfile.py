import logging
import time
from random import randint
from functools import wraps

import demo
import Ice
from locust import User, between, task


class IceClient(object):
    '''
    Simple ice client
    '''

    _locust_environment = None
    _server = None

    @property
    def host(self):
        return self.__host

    def __init__(self, host):
        self.__host = host

        communicator = Ice.initialize()
        base = communicator.stringToProxy(
            'SimpleServer:tcp -h {} -p 8000'.format(self.host))
        self._server = demo.mathPrx.checkedCast(base)
        if not self._server:
            raise RuntimeError('Invalid ice server')

    def add(self, num1, num2):
        start_time = time.time()
        try:
            return self._server.add(num1, num2)
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            self._locust_environment.events.request_failure.fire(
                request_type='ice', name='add', response_time=total_time, exception=e)
        finally:
            total_time = int((time.time() - start_time) * 1000)
            self._locust_environment.events.request_success.fire(
                request_type='ice', name='add', response_time=total_time, response_length=0)

    def substract(self, num1, num2):
        start_time = time.time()
        try:
            return self._server.substract(num1, num2)
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            self._locust_environment.events.request_failure.fire(
                request_type='ice', name='substract', response_time=total_time, exception=e)
        finally:
            total_time = int((time.time() - start_time) * 1000)
            self._locust_environment.events.request_success.fire(
                request_type='ice', name='substract', response_time=total_time, response_length=0)

    def multiply(self, num1, num2):
        start_time = time.time()
        try:
            return self._server.multiply(num1, num2)
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            self._locust_environment.events.request_failure.fire(
                request_type='ice', name='multiply', response_time=total_time, exception=e)
        finally:
            total_time = int((time.time() - start_time) * 1000)
            self._locust_environment.events.request_success.fire(
                request_type='ice', name='multiply', response_time=total_time, response_length=0)

    def divide(self, num1, num2):
        start_time = time.time()
        try:
            return self._server.divide(num1, num2)
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            self._locust_environment.events.request_failure.fire(
                request_type='ice', name='divide', response_time=total_time, exception=e)
        finally:
            total_time = int((time.time() - start_time) * 1000)
            self._locust_environment.events.request_success.fire(
                request_type='ice', name='divide', response_time=total_time, response_length=0)


class IceUser(User):
    '''
    This is the abstract User class which should be subclassed. It provides an ice client
    that can be used to make ice requests that will be tracked in Locust's statistics.
    '''
    abstract = True

    def __init__(self, *args, **kwargs):
        super(IceUser, self).__init__(*args, **kwargs)
        self.client = IceClient(self.host)
        self.client._locust_environment = self.environment


class WebsiteUser(IceUser):
    wait_time = between(1.0, 3.0)

    @task(1)
    def add(self):
        self.client.add(randint(100, 200), randint(100, 200))

    @task(1)
    def substract(self):
        self.client.substract(randint(100, 200), randint(100, 200))

    @task(1)
    def multiply(self):
        self.client.multiply(randint(100, 200), randint(100, 200))

    @task(1)
    def divide(self):
        self.client.divide(randint(100, 200), randint(100, 200))
