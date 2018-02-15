from core.base.parser import StaticParser
from core.utils import parse_hexstring
from core.base.parser import STR_TEMPLATE

ERR = [
    'No', 'WAIT1', 'Fatal w out', 'Fatal no out', 'WAIT2', 'WAIT3',
    'WAIT4', 'Last err', 'WAIT5', 'WAIT6', 'WAIT7', 'WAIT8', 'WAIT9',
    'WAIT10', 'WAIT11']


class MachineErrorParser(StaticParser):
    name = 'MSG_Machine_Error'
    event_code = '1007'

    def _make_str(self, container):
        data = parse_hexstring(container.src_data.data)
        e_type = ERR[data[0]]
        errnum = data[1]
        wide_error = (data[2] << 8) + data[3]
        context = container.src_data._asdict()
        context['message'] = '{}(Type={}, Num={}, Wide={})'.format(self.name, e_type, errnum, wide_error)
        return STR_TEMPLATE.format(**context)
