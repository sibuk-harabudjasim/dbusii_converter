# -*- coding: utf-8 -*-
import os
import re

from core.base.parser import BaseParser, STR_TEMPLATE
from parsers.utils import parse_hexstring

PUD_HEADER = 'OU_V4_CS1/app/UimoSrc/src/BL/09_SOFTWARE_UNITS/99_PUD_VAR2/06_PUD_V2_HEADER/PUD_V2_SpecificDistributorPU.h'
# PUD_HEADER = 'PUD_V2_SpecificDistributorPU.h'


class MachineEventParser(BaseParser):
    name = 'MSG_Machine_Event'
    event_code = '1000'

    def __init__(self, data):
        super().__init__(data)
        if self.data:
            self.data = {int(key): val for key, val in self.data.items()}
        else:
            self.data = {}

    def _make_str(self, container):
        evts = []
        for e in parse_hexstring(container.src_data.data):
            if not e:
                continue
            evts.append(self.data.get(e, hex(e)))
        context = container.src_data._asdict()
        context['message'] = '{}({})'.format(self.name, ','.join(evts))
        return STR_TEMPLATE.format(**context)

    def _make_json(self, container):
        return container.src_data._asdict()

    def load_data(self, root_path):
        path = os.path.join(root_path, PUD_HEADER)
        with open(path, 'r') as f:
            data = f.read()
        for name, key in re.findall(r'(M_EVENT.+?)\s=\s(\d+),', data):
            self.data[int(key)] = name

    def store_data(self):
        return self.data


__author__ = 'manitou'
