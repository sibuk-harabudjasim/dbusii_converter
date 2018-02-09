# -*- coding: utf-8 -*-

from .default import DefaultParser


def register_parsers(factory):
    factory.register_default_parser(DefaultParser)


__author__ = 'manitou'
