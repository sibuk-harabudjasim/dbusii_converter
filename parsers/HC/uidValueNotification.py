# -*- coding: utf-8 -*-
from collections import OrderedDict, deque

from core.base.parser import WithMultipleParams, STR_TEMPLATE
from core.utils import parse_hexstring
from parsers.HC.base import UIDParser


class UIDValueNotificationParser(UIDParser, WithMultipleParams):
    name = 'UIDValueNotification'
    event_code = '8831'

    def _parse_uid_valuelist_entries(self, input_data):
        out = OrderedDict()
        deq = deque(input_data)
        while deq:
            try:
                uid = (deq.popleft() << 8) + deq.popleft()
            except:
                print('corrupt valuelist:', input_data)
                return out
            uid_info = self.data.get(uid, None)
            if not uid_info:
                print('not UID info for', uid)
                print('data:', input_data)
                return out
            coerse = self._get_entry_value_coerse(uid_info)
            offset = self._get_entry_value_size(uid_info)
            try:
                val = self._collect_val(deq, coerse, offset)
            except:
                print('corrupt valuelist:', input_data)
                print('error decoding {}-th UID entry (for UID {})'.format(len(out) + 1, uid))
                return out
            out[uid_info['name']] = val
        return out

    def _parse_params(self, data):
        struct = OrderedDict()
        struct['EndDeviceID'] = data[0]
        struct['values'] = self._parse_uid_valuelist_entries(data[1:])
        return struct

    def _make_str(self, container):
        data = parse_hexstring(container.src_data.data)
        struct = self._parse_params(data)
        context = container.src_data._asdict()
        context['message'] = '{}({})'.format(self.name, self._make_dict_str(struct))
        return STR_TEMPLATE.format(**context)


__author__ = 'manitou'
