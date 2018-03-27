# -*- coding: utf-8 -*-

from .default import DefaultParser
from .machineEvent import MachineEventParser
from .OUEvent import OUEventParser
from .machineError import MachineErrorParser
from .newDeviceState import SetNewDeviceStateParser
from .setProgressStatus import SetProgressStatusParser
from .setRemainTimeIndication import SetRemainTimeIndicationParser
from .systemSynchronization import SystemSynchronizationParser
from .systemSynchronizationBlock import SystemSynchronizationBlockParser
from .sytemSynchronizationResponse import SystemSynchronizationResponseParser
from .systemSetOUValues import SystemSetOUValuesParser
from .machineDataUpdate import MachineDataUpdateParser
from .HC import (
    ProtocolVersionReadResponseParser,
    ProtocolVersionReadRequestParser,
    ComPongNotificationParser,
    HaPingPostParser,
    PingNotificationParser,
    NetStateNotificationParser
)


def register_parsers(factory):
    factory.register_parser(MachineEventParser)
    factory.register_parser(OUEventParser)
    factory.register_parser(MachineErrorParser)
    factory.register_parser(SetNewDeviceStateParser)
    factory.register_parser(SetProgressStatusParser)
    factory.register_parser(SetRemainTimeIndicationParser)
    factory.register_parser(SystemSynchronizationParser)
    factory.register_parser(SystemSynchronizationBlockParser)
    factory.register_parser(SystemSynchronizationResponseParser)
    factory.register_parser(SystemSetOUValuesParser)
    factory.register_parser(MachineDataUpdateParser)

    # HC
    factory.register_parser(ProtocolVersionReadResponseParser)
    factory.register_parser(ProtocolVersionReadRequestParser)
    factory.register_parser(ComPongNotificationParser)
    factory.register_parser(HaPingPostParser)
    factory.register_parser(PingNotificationParser)
    factory.register_parser(NetStateNotificationParser)

    factory.register_default_parser(DefaultParser)


__author__ = 'manitou'
