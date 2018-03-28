# -*- coding: utf-8 -*-


def parse_hexstring(data):
    ret = []
    for i in range(0, len(data), 2):
        ret.append(int(data[i:i+2], 16))
    return ret


def schar(val):
    return val - 0x100 if val > 0x7f else val


def sint(val):
    return val - 0x10000 if val > 0x7fff else val


def slong(val):
    return val - 0x100000000 if val > 0x7fffffff else val


def bitlist(byte):
    return [(byte >> i) & 0b1 for i in range(8)]


__author__ = 'manitou'
