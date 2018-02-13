# -*- coding: utf-8 -*-
from core.base.producer import BaseProducer


class LogFileProducer(BaseProducer):
    name = 'logfile'
    file = None

    def __init__(self, out=None):
        if not out:
            raise ValueError('"out" parameter must be specified for {}'.format(self.__class__.__name__))
        self.out_filename = out

    def __enter__(self):
        self.file = open(self.out_filename, 'w')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            self.file = None

    def output(self, container):
        if not self.file:
            raise ValueError('use of output() outside of context manager')
        self.file.write(container.str() + '\n')


class ReplacingLogFileProducer(LogFileProducer):
    name = 'logfile_replace'
    vfile = None

    def __enter__(self):
        self.vfile = ''
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.vfile:
            file = open(self.out_filename, 'w')
            file.write(self.vfile)
            file.close()

    def output(self, container):
        self.vfile += container.str() + '\n'


__author__ = 'manitou'
