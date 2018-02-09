# -*- coding: utf-8 -*-

# receives list of containers
# stores to file or stream


class BaseProducer(object):
    name = None

    def __init__(self, out=None):
        '''
        Set output options
        :param args:
        :param kwargs:
        '''
        pass

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError

    def output(self, container):
        '''
        Stores item in output file, stream, whatever
        :param container: event container
        :return: None
        '''
        raise NotImplementedError


__author__ = 'manitou'
