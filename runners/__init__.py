# -*- coding: utf-8 -*-
from .simple_runner import SimpleRunner, ReplaceRunner

RUNNERS = [
    SimpleRunner,
    ReplaceRunner
]

runners_map = {r.name: r for r in RUNNERS}


def get_runner(name):
    return runners_map.get(name, None)


__author__ = 'manitou'
