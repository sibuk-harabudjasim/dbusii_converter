# -*- coding: utf-8 -*-
from consumers.logfile import LogFileConsumer
from core.base.runner import BaseRunner
from producers import LogFileProducer


class SimpleRunner(BaseRunner):
    name = 'simple'
    consumer = LogFileConsumer
    producer = LogFileProducer


__author__ = 'manitou'
