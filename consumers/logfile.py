# -*- coding: utf-8 -*-
from core.base.consumer import BaseConsumer
from core.base.container import log_entry


ACK_KEYWORDS = {
    'ACK_OK': 'OK',
    'ACK_Timeout': 'TOUT',
    'RX_Collision': 'COL',
    'Undefined Ack': 'UND'
}


class LogFileConsumer(BaseConsumer):
    name = 'logfile'
    file = None

    def __init__(self, in_=None):
        if not in_:
            raise ValueError('"in" parameter must be specified for {}'.format(self.__class__.__name__))
        self.in_filename = in_

    def __enter__(self):
        self.file = open(self.in_filename, 'r')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            self.file = None

    @staticmethod
    def _parse_line(line):
        ack = [v for kw, v in ACK_KEYWORDS.items() if kw in line]
        if ack:
            return {'ack': ack[0]}, True
        chunks = [c.strip() for c in line.split('\t')]
        # timestamp sr len id data par sub crc message
        return {
            'timestamp': chunks[0],
            'length': chunks[2],
            'id': chunks[3],
            'data': chunks[4],
            'par': chunks[5],
            'sub': chunks[6],
            'crc': chunks[7],
            'message': chunks[8],
        }, False

    def input(self):
        if not self.file:
            raise ValueError('use of input() outside of context manager')
        line_data = {}
        for line in self.file.readlines():
            line = line.strip()
            if line.startswith('Time'):
                continue
            if not line:
                continue
            new_data, is_ack = self._parse_line(line)
            line_data.update(new_data)
            if is_ack:
                yield log_entry(**line_data)
                line_data = {}
        if line_data:
            yield log_entry(**line_data)


__author__ = 'manitou'
