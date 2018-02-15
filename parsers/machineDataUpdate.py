from core.base.parser import StaticParser
from core.utils import parse_hexstring
from core.base.parser import STR_TEMPLATE

DOOR_STATUS = {
    0x00: 'STATUS_OPEN',
    0x01: 'STATUS_UNLOCKED',
    0x11: 'STATUS_UNLOCKED_NOLOCK',
    0x02: 'STATUS_LOCKED_SAFE',
    0x12: 'STATUS_LOCKED_UNSAFE',
    0x33: 'STATUS_OPEN_LOCKED_UNSAFE'
}


def _actual_drum_speed(data):
    res = 'actual_Drum_speed={}'.format((data[0] << 8) + data[1])
    if data[0] or data[1]:
        res += ', rotation={}'.format('right' if data[2] else 'left')
    return res


MACHINE_DATA = {
    1: lambda data: 'door_status={}'.format(DOOR_STATUS[data[0]]),
    2: lambda data: 'drain_pump_status={}'.format('on' if data[0] else 'off'),
    3: lambda data: 'circulation_pump_status={}'.format('on' if data[0] else 'off'),
    4: lambda data: 'water_heater_status={}'.format('on' if data[0] else 'off'),
    5: lambda data: '1_prewash_valve_status={}'.format('on' if data[0] else 'off'),
    6: lambda data: '2_mainwash_valve_status={}'.format('on' if data[0] else 'off'),
    7: lambda data: '3_warm_water_status={}'.format('on' if data[0] else 'off'),
    8: lambda data: '4_flushing_valve_status={}'.format('on' if data[0] else 'off'),
    9: lambda data: '5_cooling_valve_status={}'.format('on' if data[0] else 'off'),
    10: lambda data: 'target_drum_speed={}'.format((data[0] << 8) + data[1]),
    11: _actual_drum_speed,
    12: lambda data: 'pressure_value={}'.format((data[0] << 8) + data[1]),
    13: lambda data: 'water_temperature={}C'.format((data[0] << 8) + data[1]),
    14: lambda data: 'T_HEATAIR={}C'.format(((data[0] << 8) + data[1]) / 10.0),
    15: lambda data: 'T_VALUE_2={}C'.format(((data[0] << 8) + data[1]) / 10.0),
    16: lambda data: 'T_VALUE_3={}C'.format(((data[0] << 8) + data[1]) / 10.0),
    17: lambda data: 'idos_pump_1_status={}'.format('on' if data[0] else 'off'),
    18: lambda data: 'idos_pump_2_status={}'.format('on' if data[0] else 'off'),
    19: lambda data: 'FOAM_DETECTED={}'.format(str(bool(data[0]))),
    20: lambda data: 'flow_rate_cold={}L/min'.format(data[0] / 10.0),
    21: lambda data: 'flow_rate_warm={}L/min'.format(data[0] / 10.0),
    22: lambda data: 'MLD_LOAD={}'.format((data[0] << 8) + data[1]),
    23: lambda data: 'CURRENT_STWF_NUMBER={}'.format((data[0] << 8) + data[1]),
    24: lambda data: 'WATER_QUANTITY={}'.format((data[0] << 8) + data[1])
}

class MachineDataUpdateParser(StaticParser):
    name = 'MSG_Machine_Data_Update'
    event_code = '1811'

    def _parse_value(self, data):
        data_typ = (data[0] << 8) + data[1]
        return MACHINE_DATA[data_typ](data[2:])

    def _make_str(self, container):
        data = parse_hexstring(container.src_data.data)
        context = container.src_data._asdict()
        context['message'] = '{}({})'.format(self.name, self._parse_value(data))
        return STR_TEMPLATE.format(**context)
