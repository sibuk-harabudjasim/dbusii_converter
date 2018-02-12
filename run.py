# -*- coding: utf-8 -*-

from consumers import get_consumer
from core.optparse import get_options
from core.parser_factory import ParserFactory
from producers import get_producer
from runners import get_runner

CONFIG_FILE = './config.json'

if __name__ == '__main__':
    options = get_options(defaults={
        'runner': 'simple',
        'configfile': CONFIG_FILE
    })
    parser_factory = ParserFactory()

    if options.make_config:
        print('Storing config to \'{}\' from \'{}\''.format(options.configfile, options.make_config))
        parser_factory.make_config(options.make_config, options.configfile)
        exit(0)

    parser_factory.init_parsers(options.configfile)
    runner_cls = get_runner(options.runner)
    if not runner_cls:
        print('Error: no such runner \'{}\''.format(options.runner))
        exit(-1)
    runner = runner_cls(parser_factory)

    if options.consumer:
        consumer = get_consumer(options.consumer)
        if not consumer:
            print('Error: no such consumer \'{}\''.format(options.consumer))
            exit(-1)
        runner.consumer = consumer

    producer_name = options.producer or ('logfile' if options.out else 'stdout')
    producer = get_producer(producer_name)
    if not producer:
        print('Error: no such producer \'{}\''.format(producer_name))
        exit(-1)
    runner.producer = producer

    runner.run(options.in_, options.out)


__author__ = 'manitou'
