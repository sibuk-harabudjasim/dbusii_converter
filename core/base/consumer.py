# -*- coding: utf-8 -*-

# processes input file
# returns list of entries


class BaseConsumer(object):
    '''Base class for consumer which will provide information to parse'''
    name = None

    def __init__(self, in_=None):
        '''
        Receives consume options
        :param args:
        :param kwargs:
        '''
        raise NotImplementedError

    def __enter__(self):
        raise NotImplementedError

    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError

    def input(self):
        '''
        generator that produce entries
        :return: None
        '''
        raise NotImplementedError


__author__ = 'manitou'
