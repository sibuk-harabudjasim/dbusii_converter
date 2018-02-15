from core.base.parser import StaticParser
from core.utils import parse_hexstring
from core.base.parser import STR_TEMPLATE

class SetRemainTimeIndicationParser(StaticParser):
    name = 'MSG_Set_Remain_Time_Indication'
    event_code = '1002'

    def _make_str(self, container):
        data = parse_hexstring(container.src_data.data)
        remain_time = (data[0] << 8) + data[1]
        context = container.src_data._asdict()
        context['message'] = '{}({})'.format(self.name, remain_time)
        return STR_TEMPLATE.format(**context)
