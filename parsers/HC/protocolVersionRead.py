# -*- coding: utf-8 -*-
from core.base.parser import StaticParser, STR_TEMPLATE
from core.utils import parse_hexstring


class ProtocolVersionReadRequestParser(StaticParser):
    name = 'ProtocolVersionReadRequest'
    event_code = '8000'

    def _make_str(self, container):
        data = parse_hexstring(container.src_data.data)
        context = container.src_data._asdict()
        context['message'] = '{}({}.{})'.format(self.name, data[0], data[1])
        return STR_TEMPLATE.format(**context)


class ProtocolVersionReadResponseParser(StaticParser):
    name = 'ProtocolVersionReadResponse'
    event_code = '8200'

    def _make_str(self, container):
        data = parse_hexstring(container.src_data.data)
        context = container.src_data._asdict()
        context['message'] = '{}({}.{})'.format(self.name, data[0], data[1])
        return STR_TEMPLATE.format(**context)


__author__ = 'manitou'
