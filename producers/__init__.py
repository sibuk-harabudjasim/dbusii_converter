# -*- coding: utf-8 -*-
from .logfile import LogFileProducer, ReplacingLogFileProducer
from .stdout import StdoutProducer

PRODUCERS = [
    LogFileProducer,
    ReplacingLogFileProducer,
    StdoutProducer
]

producers_map = {p.name: p for p in PRODUCERS}


def get_producer(name):
    return producers_map.get(name, None)


__author__ = 'manitou'
