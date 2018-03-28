# -*- coding: utf-8 -*-
import os
import re

from core.base.parser import MapBasedParser

PUD_HEADER = 'OU_V4_CS1/app/UimoSrc/src/BL/09_SOFTWARE_UNITS/99_PUD_VAR2/06_PUD_V2_HEADER/PUD_V2_SpecificDistributorPU.h'
# PUD_HEADER = 'PUD_V2_SpecificDistributorPU.h'


class OUBasedParser(MapBasedParser):
    name = 'MSG_OU_Event'
    event_code = '1001'

    def load_data(self, root_path):
        path = os.path.join(root_path, PUD_HEADER)
        with open(path, 'r') as f:
            data = f.read()
        for name, key in re.findall(r'(OU_EVENT.+?)\s?=\s?(\d+),', data):
            self.data[int(key)] = name


__author__ = 'manitou'
