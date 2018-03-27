# -*- coding: utf-8 -*-
from core.base.parser import StaticParser, STR_TEMPLATE


class PingNotificationParser(StaticParser):
    name = 'PingNotification'
    event_code = '8800'

    def _make_str(self, container):
        context = container.src_data._asdict()
        context['message'] = self.name
        return STR_TEMPLATE.format(**context)


class HaPingPostParser(StaticParser):
    name = 'HaPingPost'
    event_code = '8A07'

    def _make_str(self, container):
        context = container.src_data._asdict()
        context['message'] = self.name
        return STR_TEMPLATE.format(**context)


class ComPongNotificationParser(StaticParser):
    name = 'ComPongNotification'
    event_code = '8807'

    def _make_str(self, container):
        context = container.src_data._asdict()
        context['message'] = self.name
        return STR_TEMPLATE.format(**context)


__author__ = 'manitou'
