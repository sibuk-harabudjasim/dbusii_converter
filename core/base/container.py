# -*- coding: utf-8 -*-

# stores entry data

# entry structure

# container structure
from collections import namedtuple

log_entry = namedtuple('LogEntry', 'timestamp length id data par sub crc message ack')


class EventContainer(object):
    '''
    Container for holding parsed log data
    '''
    valid = None
    timestamp = None
    id = None
    src_data = None

    def __init__(self, src):
        self.src_data = src

    def str(self):
        '''Provides string representation of entry. Must be replaced by parser method!'''
        raise NotImplementedError

    def json(self):
        '''Provides JSON compatible representation of entry. Must be replaced by parser!'''
        raise NotImplementedError


__author__ = 'manitou'
