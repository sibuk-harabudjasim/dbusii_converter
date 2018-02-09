# -*- coding: utf-8 -*-
from .logfile import LogFileConsumer

CONSUMERS = [
    LogFileConsumer
]

consumers_map = {c.name: c for c in CONSUMERS}


def get_consumer(name):
    return consumers_map.get(name, None)


__author__ = 'manitou'
