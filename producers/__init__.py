# -*- coding: utf-8 -*-
from .logfile import LogFileProducer
from .stdout import StdoutProducer

PRODUCERS = [
    LogFileProducer,
    StdoutProducer
]

producers_map = {p.name: p for p in PRODUCERS}


def get_producer(name):
    return producers_map.get(name, None)


__author__ = 'manitou'
