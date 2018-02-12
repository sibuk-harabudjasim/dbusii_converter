# -*- coding: utf-8 -*-


def parse_hexstring(data):
    ret = []
    for i in range(0, len(data), 2):
        ret.append(int(data[i:i+2], 16))
    return ret


__author__ = 'manitou'
