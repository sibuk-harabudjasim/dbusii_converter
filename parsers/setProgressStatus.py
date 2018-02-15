from core.base.parser import StaticParser
from core.utils import parse_hexstring
from core.base.parser import STR_TEMPLATE

class SetProgressStatusParser(StaticParser):
    name = 'MSG_Set_Progress_Status'
    event_code = '1003'

    def _make_str(self, container):
        data = parse_hexstring(container.src_data.data)
        context = container.src_data._asdict()
        context['message'] = '{}({})'.format(self.name, data[0])
        return STR_TEMPLATE.format(**context)
