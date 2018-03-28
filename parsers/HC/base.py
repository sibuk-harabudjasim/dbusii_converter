# -*- coding: utf-8 -*-
import os
import re
from collections import deque

from core.base.parser import MapBasedParser
from core.utils import schar, sint, slong

UIDS_HEADER = 'OU_V4_CS1/app/UimoSrc/src/BL/09_SOFTWARE_UNITS/01_COMMON_HEADERS/CFG_HFC_FeatureConfiguration.h'
# UIDS_HEADER = 'CFG_HFC_FeatureConfiguration.h'


class UIDParser(MapBasedParser):
    def load_data(self, root_path):
        path = os.path.join(root_path, UIDS_HEADER)
        with open(path, 'r') as f:
            data = f.read()
        # erase comments (remove commented code)
        data = re.sub(r'\/\*.+?\*\/', '', data)
        lambdas = re.findall(r'HC_LAMBDA_FEATURE_CONFIG\s?\((.+?)\)', data)
        for line in lambdas:
            chunks = [i.strip() for i in line.split(',')]
            uid_match = re.match(r'=\s(.+)', chunks[1])
            if not uid_match:
                print('no UID in line', line)
                continue
            uid = uid_match.group(1)
            int_uid = int(uid, 16)
            self.data[int_uid] = {
                'uid': uid,
                'name': chunks[0],
                'type': chunks[8]
            }

    def _parse_uid_entries(self, input_data):
        if len(input_data) % 2:
            print('wrong length of data')
            return []
        out = []
        deq = deque(input_data)
        while deq:
            out.append((deq.popleft() << 8) + deq.popleft())
        return out

    @staticmethod
    def _get_entry_value_size(uid_info):
        return {
            'B': 1,
            'UC': 1,
            'UI': 2,
            'SC': 1,
            'SI': 2,
            'UL': 4,
            'SL': 4
        }.get(uid_info['type'], 0)

    @staticmethod
    def _get_entry_value_coerse(uid_info):
        return {
            'B': lambda val: 'True' if val else 'False',
            'UC': int,
            'UI': int,
            'SC': schar,
            'SI': sint,
            'UL': int,
            'SL': slong
        }.get(uid_info['type'], int)

    @staticmethod
    def _collect_val(deq, coerse, length):
        val = 0
        for i in range(length):
            val = (val << 8) + deq.popleft()
        return coerse(val)


__author__ = 'manitou'
