# -*- coding: utf-8 -*-
from consumers.logfile import LogFileConsumer
from core.base.runner import BaseRunner
from producers import LogFileProducer, ReplacingLogFileProducer


class SimpleRunner(BaseRunner):
    name = 'simple'
    consumer = LogFileConsumer
    producer = LogFileProducer


class ReplaceRunner(BaseRunner):
    name = 'replace'
    consumer = LogFileConsumer
    producer = ReplacingLogFileProducer


__author__ = 'manitou'
