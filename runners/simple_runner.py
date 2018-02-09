# -*- coding: utf-8 -*-
from consumers.logfile import LogFileConsumer
from core.base.runner import BaseRunner
from producers.stdout import StdoutProducer


class SimpleRunner(BaseRunner):
    name = 'simple'
    consumer = LogFileConsumer
    producer = StdoutProducer


__author__ = 'manitou'
