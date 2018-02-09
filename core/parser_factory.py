# -*- coding: utf-8 -*-
import json


class ParserFactory(object):
    '''
    Factory that holds all parsers, loads stored data
    '''
    registered_parsers = []
    default_parser_cls = None

    def __init__(self):
        self.parsers = {}
        self.default_parser = None
        self._load_parsers()

    @classmethod
    def register_parser(cls, parser_class):
        cls.registered_parsers.append(parser_class)

    @classmethod
    def register_default_parser(cls, parser_class):
        cls.default_parser_cls = parser_class

    def _load_parsers(self):
        from parsers import register_parsers
        register_parsers(self)

    def init_parsers(self, configfile):
        with open(configfile) as f:
            config = json.loads(f.read())

        available_parsers = {p.name: p for p in self.registered_parsers}
        for name, data in config.items():
            parser_cls = available_parsers.get(name, None)
            if not parser_cls:
                continue
            self.parsers[parser_cls.event_code] = parser_cls(data)
        if self.default_parser_cls:
            self.default_parser = self.default_parser_cls(None)

    def get(self, event_code):
        return self.parsers.get(event_code, self.default_parser)

    def make_config(self, root_path, configfile):
        config_data = {}
        for parser_cls in self.registered_parsers:
            parser = parser_cls(None)
            parser.load_data(root_path)
            config_data[parser.name] = parser.store_data()
        with open(configfile, 'w') as f:
            f.write(json.dumps(config_data))


__author__ = 'manitou'
