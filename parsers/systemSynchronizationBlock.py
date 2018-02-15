from core.base.parser import StaticParser
from core.utils import parse_hexstring
from core.base.parser import STR_TEMPLATE

BLOCK = ['ID_BLOCK', 'VARIANT_BLOCK', 'VT_BLOCK']


class SystemSynchronizationBlockParser(StaticParser):
    name = 'MSG_System_Synchronization_Block'
    event_code = '100B'

    def _make_str(self, container):
        data = parse_hexstring(container.src_data.data)
        context = container.src_data._asdict()
        context['message'] = '{}(Type={}, BlockNum={})'.format(self.name, BLOCK[data[0]], data[1])
        return STR_TEMPLATE.format(**context)
