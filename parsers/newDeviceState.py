from collections import OrderedDict
from core.base.parser import StaticParser
from core.utils import parse_hexstring
from core.base.parser import STR_TEMPLATE

SOIL = ['V1', 'V2', 'V3', '']
IDOS = ['off', 'on-low', 'on', 'on-high']
LOAD = ['auto', 'less', 'half', 'full']
DRY_FUNC = ['no_add', '120', '90', '60', '30', '15', 'extra', 'cupboard', 'light', 'timedry', '', '', '', '', '', '']
DRY_TEMP = ['gentle', 'intensive', 'intensive_2']
DRY_PTYPE = ['solo_wash', 'combined', 'solo_dry', '']


class SetNewDeviceStateParser(StaticParser):
    name = 'MSG_Set_New_Device_State'
    event_code = '1006'

    def _parse_data(self, data):
        struct = OrderedDict()
        struct['ProgID'] = data[0]
        struct['SpinSpeed'] = data[1]
        struct['TempStep'] = data[2]
        # level
        soil = data[3] & 0b11
        idos1 = (data[3] >> 2) & 0b11
        idos2 = (data[3] >> 4) & 0b11
        load = (data[3] >> 6) & 0b11
        level = OrderedDict([
            ('Soil', SOIL[soil]),
            ('IDOS_1', IDOS[idos1]),
            ('IDOS_2', IDOS[idos2]),
            ('Load', LOAD[load])
        ])
        struct['Level'] = level
        struct['AddOpt'] = 'RinseHoldActive' if data[4] & 1 else 'RinseHoldInactive'
        struct['ProcOpts'] = list(map(bin, [data[7], data[5], data[6]]))
        if len(data) > 8:
            #drying settings
            func = data[8] & 0b1111
            temp = (data[8] >> 4) & 0b11
            ptype = (data[8] >> 6) & 0b11
            dry = bin(data[9])
            drying = OrderedDict([
                ('DryFunc', DRY_FUNC[func]),
                ('DryTemp', DRY_TEMP[temp]),
                ('DryType', DRY_PTYPE[ptype]),
                ('DryOpts2', dry)
            ])
            struct['WashDryOpts'] = drying
            if len(data) > 10:
                struct['ProgRefID'] = data[10]
                if len(data) > 11:
                    struct['UniqProgID'] = (data[11] << 8) + data[12]
        return struct

    def _make_dict_str(self, data):
        res = []
        for key, val in data.items():
            fmt = '{}({})' if isinstance(val, OrderedDict) else '{}={}'
            res.append(fmt.format(key, self._make_val_str(val)))
        return ', '.join(res)

    def _make_val_str(self, val):
        if isinstance(val, OrderedDict):
            return self._make_dict_str(val)
        elif isinstance(val, list):
            return '[' + ', '.join([self._make_val_str(v) for v in val]) + ']'
        else:
            return str(val)

    def _make_str(self, container):
        data = parse_hexstring(container.src_data.data)
        struct = self._parse_data(data)
        context = container.src_data._asdict()
        context['message'] = '{}({})'.format(self.name, self._make_dict_str(struct))
        return STR_TEMPLATE.format(**context)
