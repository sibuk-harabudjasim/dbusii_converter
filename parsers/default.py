# -*- coding: utf-8 -*-
from core.base.parser import BaseParser, STR_TEMPLATE


class DefaultParser(BaseParser):
    name = 'default'

    def _make_str(self, container):
        return STR_TEMPLATE.format(**container.src_data._asdict())

    def _make_json(self, container):
        return container.src_data._asdict()

    def load_data(self, root_path):
        pass

    def store_data(self):
        return {}


__author__ = 'manitou'
