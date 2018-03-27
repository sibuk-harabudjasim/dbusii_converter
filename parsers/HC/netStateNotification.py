# -*- coding: utf-8 -*-
from collections import OrderedDict

from core.base.parser import StaticParser, STR_TEMPLATE, WithMultipleParams
from core.utils import parse_hexstring


WIFI_PARAMS = [
    'ServiceAPConnected', None, 'SapConfigRunning', 'SsidPwdSecure',
    'WifiConnected', 'StoredWifiNet', 'WpsRunning', 'WifiModuleState'
]

PHYSICAL_CONNECTIONS = [None] * 12 + [
    'ShipDevice', 'EndDevice', 'CustomerDevice', 'BackendConnected'
]

ADDITIONAL_ATTRIBUTES = [None] * 7 + ['EndDevicePaired'] + [None] * 4 + [
    'BlackoutPreventionBinded', 'LoadManagementBinded', 'FlexStartBinded',
    'CEMPaired'
]


def _parse_one_param(val, struct):
    out = OrderedDict()
    for i, name in enumerate(struct):
        if name:
            out[name] = (val >> i) & 0b1
    return out


def _parse_rssi(val):
    return val - 256 if val > 127 else val


class NetStateNotificationParser(StaticParser, WithMultipleParams):
    name = 'NetStateNotification'
    event_code = '8801'

    def _parse_params(self, data):
        struct = OrderedDict()
        struct['WifiState'] = _parse_one_param(data[0], WIFI_PARAMS)
        physical = (data[1] << 8) + data[2]
        struct['PhysicalConnections'] = _parse_one_param(physical, PHYSICAL_CONNECTIONS)
        additional = (data[3] << 8) + data[4]
        struct['AdditionalAttrs'] = _parse_one_param(additional, ADDITIONAL_ATTRIBUTES)
        struct['RSSI'] = _parse_rssi(data[5])
        return struct

    def _make_str(self, container):
        data = parse_hexstring(container.src_data.data)
        struct = self._parse_params(data)
        context = container.src_data._asdict()
        context['message'] = '{}({})'.format(self.name, self._make_dict_str(struct))
        return STR_TEMPLATE.format(**context)


__author__ = 'manitou'
