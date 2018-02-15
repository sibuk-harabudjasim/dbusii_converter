from core.base.parser import StaticParser
from core.utils import parse_hexstring
from core.base.parser import STR_TEMPLATE

VAL = [
    'REMAIN_TIME_BEHAVIOR', 'WEIGHT_MEASUREMENT_VALUE', 'FACTORY_TEST_VARIANT',
    'START_DISPLAY_LED_TEST', 'IDOS_AGENT_LEVEL', 'MINIMUM_REMAIN_TIME', '', '', '',
    '', '', 'HC_PARAMETER', '', 'PU_APPLICATION_COOL_DOWN_STATE'
]

PU = ['IDLE', 'PRE_COOLDOWN_PHASE', 'COOLDOWN_RUNNING']


class SystemSetOUValuesParser(StaticParser):
    name = 'MSG_System_Set_OU_Values'
    event_code = '1004'

    def _parse_value(self, data):
        typ = VAL[data[0]]
        if typ == 'REMAIN_TIME_BEHAVIOR':
            return 'startTime={}, amplitude={}, progRefID={}'.format(*data[1:])
        if typ == 'WEIGHT_MEASUREMENT_VALUE':
            return str((data[1] << 8) & data[2])
        if typ == 'FACTORY_TEST_VARIANT':
            return str(data[1])
        if typ == 'START_DISPLAY_LED_TEST':
            return str(data[1])
        if typ == 'IDOS_AGENT_LEVEL':
            trays = ['filled' if d else 'empty' for d in data[1:3]]
            return 'tray1={}, tray2={}'.format(*trays)
        if typ == 'MINIMUM_REMAIN_TIME':
            return '{}, progRefID={}'.format((data[1] << 8) & data[2], data[3])
        if typ == 'HC_PARAMETER':
            wifi = ['no WIFI', 'Worldwide', 'US', 'EU', 'AP'][data[1]]
            energy = []
            if data[2] & 1:
                energy.append('Emergency shutdown')
            if (data[2] >> 1) & 1:
                energy.append('Load reduction')
            if (data[2] >> 2) & 1:
                energy.append('Flex start')
            if (data[2] >> 3) & 1:
                energy.append('Forecast')
            return 'WIFI={}, EnergyMangerOptions={}'.format(wifi, '[' + ', '.join(energy) + ']')
        if typ == 'PU_APPLICATION_COOL_DOWN_STATE':
            return PU[data[1]]
        return str(data[0])

    def _make_str(self, container):
        data = parse_hexstring(container.src_data.data)
        context = container.src_data._asdict()
        context['message'] = '{}({}, {})'.format(self.name, VAL[data[0]], self._parse_value(data))
        return STR_TEMPLATE.format(**context)