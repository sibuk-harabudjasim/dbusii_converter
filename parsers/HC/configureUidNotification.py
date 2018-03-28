# -*- coding: utf-8 -*-
import traceback
from collections import OrderedDict, deque

from core.base.parser import WithMultipleParams, STR_TEMPLATE
from core.utils import parse_hexstring, bitlist
from parsers.HC.base import UIDParser


ATTRIBUTES = [
    'Avail', 'Access', 'EnumTyp', 'Exec', 'Min', 'Max', 'Step', 'Def'
]


class ConfigureUIDNotificationParser(UIDParser, WithMultipleParams):
    name = 'ConfigureUIDNotification'
    event_code = '8832'

    def _parse_attr_val(self, attr_name, val):
        return {
            'Avail': lambda _val: 'True' if _val else 'False',
            'Access': lambda _val: ['-', 'R', 'RW', 'W'][_val],
            'Exec': lambda _val: ['-', 'Select', 'Start', 'Select&Start'][_val]
        }.get(attr_name, lambda _val: _val)(val)

    def _get_fixed_attr_len(self, attr_name):
        if attr_name in ['Avail', 'Access', 'Exec']:
            return 1
        if attr_name == 'EnumTyp':
            return 2

    def _parse_configure_uid_list_entries(self, input_data):
        out = OrderedDict()
        deq = deque(input_data)
        while deq:
            try:
                uid = (deq.popleft() << 8) + deq.popleft()
            except:
                print('corrupt valuelist (uid):', input_data)
                return out
            uid_info = self.data.get(uid, None)
            if not uid_info:
                print('not UID info for', uid)
                print('data:', input_data)
                return out
            coerse = self._get_entry_value_coerse(uid_info)
            value_len = self._get_entry_value_size(uid_info)
            struct = OrderedDict()
            # struct['UID'] = hex(uid)

            try:
                group_uid = (deq.popleft() << 8) + deq.popleft()
            except:
                print('corrupt valuelist (group_uid):', input_data)
                return out
            # struct['GroupUID'] = hex(group_uid)

            try:
                attrs = bitlist(deq.popleft())
            except:
                print('corrupt valuelist (attrs):', input_data)
                return out
            attrs = list(reversed(attrs))
            for i, attr_name in enumerate(ATTRIBUTES):
                if attrs[i]:
                    try:
                        attr_val_len = self._get_fixed_attr_len(attr_name) or value_len
                        attr_val = self._collect_val(deq, coerse, attr_val_len)
                        attr_val = self._parse_attr_val(attr_name, attr_val)
                    except Exception as e:
                        print(traceback.format_exc())
                        print('corrupt valuelist ({}): {} ({})'.format(attr_name, attr_val, type(attr_val)))
                        print(input_data)
                        print(deq)
                        break
                    struct[attr_name] = attr_val
            out[uid_info['name']] = struct
        return out

    def _parse_params(self, data):
        struct = OrderedDict()
        struct['UIDS'] = self._parse_configure_uid_list_entries(data)
        return struct

    def _make_str(self, container):
        data = parse_hexstring(container.src_data.data)
        struct = self._parse_params(data)
        context = container.src_data._asdict()
        context['message'] = '{}({})'.format(self.name, self._make_dict_str(struct))
        return STR_TEMPLATE.format(**context)


__author__ = 'manitou'
