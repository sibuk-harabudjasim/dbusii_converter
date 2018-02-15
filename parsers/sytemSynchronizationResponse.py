from core.base.parser import StaticParser
from core.utils import parse_hexstring
from core.base.parser import STR_TEMPLATE

RESP = ['OK', 'VT_INVALID', '', '', 'ERROR', 'RESET_REQUEST']


class SystemSynchronizationResponseParser(StaticParser):
    name = 'MSG_System_Synchronization_Response'
    event_code = '100C'

    def _make_str(self, container):
        data = parse_hexstring(container.src_data.data)
        context = container.src_data._asdict()
        context['message'] = '{}({})'.format(self.name, RESP[data[0]])
        return STR_TEMPLATE.format(**context)
