from core.base.parser import StaticParser
from core.utils import parse_hexstring
from core.base.parser import STR_TEMPLATE

SYNC = [
    'GET_ID_STRING', 'PREPARE_FOR_VT_UPDATE', 'VT_UPDATE_FINISH',
    'VARIANT_START', 'VARIANT_FINISH', '', 'NO_VT_UPDATE_NEEDED'
]


class SystemSynchronizationParser(StaticParser):
    name = 'MSG_System_Synchronization'
    event_code = '100A'

    def _make_str(self, container):
        data = parse_hexstring(container.src_data.data)
        context = container.src_data._asdict()
        context['message'] = '{}({})'.format(self.name, SYNC[data[0]])
        return STR_TEMPLATE.format(**context)
