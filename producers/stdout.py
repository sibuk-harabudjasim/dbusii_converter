# -*- coding: utf-8 -*-
from core.base.parser import STR_HEADER
from core.base.producer import BaseProducer


class StdoutProducer(BaseProducer):
    name = 'stdout'

    def __init__(self, out=None):
        pass

    def __enter__(self):
        print(STR_HEADER + '\n')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def output(self, container):
        print(container.str())


__author__ = 'manitou'
