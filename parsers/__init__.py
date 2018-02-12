# -*- coding: utf-8 -*-

from .default import DefaultParser
from .machineEvent import MachineEventParser
from .OUEvent import OUEventParser


def register_parsers(factory):
    factory.register_parser(MachineEventParser)
    factory.register_parser(OUEventParser)
    factory.register_default_parser(DefaultParser)


__author__ = 'manitou'
