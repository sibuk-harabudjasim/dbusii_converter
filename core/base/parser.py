# -*- coding: utf-8 -*-

# processes entry, return container or output string (several formats)
# also have storage. have to be able to parse source, store and load data from storage
from core.base.container import EventContainer
from core.utils import parse_hexstring

STR_HEADER = 'Timestamp\tLen\tID\tPar\tSub\tACK\tMessage\t\tData'
STR_TEMPLATE = '{timestamp}\t{length}\t{id}\t{par}\t{sub}\t{ack}\t{message}\t{data}'


class BaseParser(object):
    '''Base class for parsing particular event'''
    name = None
    event_code = None

    def __init__(self, data):
        '''Prepare stored data for using in parse'''
        self.data = data

    def _make_str(self, container):
        '''Makes string presentation of event container'''
        raise NotImplementedError

    def _make_json(self, container):
        '''Makes JSON compatible presentation of event container'''
        raise NotImplementedError

    def _inject_makes(self, container):
        '''Injects presentation methods into container'''
        container.str = lambda: self._make_str(container)
        container.json = lambda: self._make_json(container)
        return container

    def process(self, entry):
        '''Parse entry and provide container with proper described event'''
        container = EventContainer(entry)
        container.id = entry.id
        container.timestamp = entry.timestamp
        container.valid = True
        return self._inject_makes(container)

    def load_data(self, root_path):
        '''
        Parse source code and prepare data for parsing
        :param root_path: path to root folder of project
        :return: None
        '''
        raise NotImplementedError

    def store_data(self):
        '''Returns inner data in JSON compatible format for storing'''
        raise NotImplementedError


class MapEventParser(BaseParser):
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
            evts.append(self.data.get(e, str(e)))
        context = container.src_data._asdict()
        context['message'] = '{}({})'.format(self.name, ','.join(evts))
        return STR_TEMPLATE.format(**context)

    def _make_json(self, container):
        return container.src_data._asdict()

    def store_data(self):
        return self.data


__author__ = 'manitou'
