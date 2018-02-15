# -*- coding: utf-8 -*-

from .default import DefaultParser
from .machineEvent import MachineEventParser
from .OUEvent import OUEventParser
from .machineError import MachineErrorParser
from .newDeviceState import SetNewDeviceStateParser
from .setProgressStatus import SetProgressStatusParser
from .setRemainTimeIndication import SetRemainTimeIndicationParser
from .systemSynchronization import SystemSynchronizationParser


def register_parsers(factory):
    factory.register_parser(MachineEventParser)
    factory.register_parser(OUEventParser)
    factory.register_parser(MachineErrorParser)
    factory.register_parser(SetNewDeviceStateParser)
    factory.register_parser(SetProgressStatusParser)
    factory.register_parser(SetRemainTimeIndicationParser)
    factory.register_parser(SystemSynchronizationParser)
    factory.register_default_parser(DefaultParser)


__author__ = 'manitou'
