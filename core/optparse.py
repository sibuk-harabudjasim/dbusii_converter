# -*- coding: utf-8 -*-
from optparse import OptionParser


DESCRIPTION = '''
DBus-II log converter
'''


def get_options(defaults=None):
    parser = OptionParser(description=DESCRIPTION)
    parser.set_defaults(**(defaults or {}))
    parser.add_option('--make-config', dest='make_config', help='no conversion, only make config from source', metavar='ROOT_DIR')
    parser.add_option('-c', '--config', dest='configfile', help='config file for converter', metavar='FILE')
    parser.add_option('-i', '--in', dest='in_', help='input parameters for consumer', metavar='PARAMS')
    parser.add_option('-o', '--out', dest='out', help='output parameters for producer', metavar='PARAMS')
    parser.add_option('--consumer', dest='consumer', help='use custom consumer', metavar='NAME')
    parser.add_option('--producer', dest='producer', help='use custom producer', metavar='NAME')
    parser.add_option('-r', '--runner', dest='runner', help='user custom runner', metavar='NAME')
    options, args = parser.parse_args()
    return options


__author__ = 'manitou'
