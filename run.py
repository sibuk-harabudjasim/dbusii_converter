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
    custom_runner = options.consumer or options.producer
    if custom_runner:
        if options.consumer:
            consumer = get_consumer(options.consumer)
            if not consumer:
                print('Error: no such consumer \'{}\''.format(options.consumer))
                exit(-1)
            runner.consumer = consumer
        if options.producer:
            producer = get_producer(options.producer)
            if not producer:
                print('Error: no such producer \'{}\''.format(options.producer))
                exit(-1)
            runner.producer = producer

    runner.run(options.in_, options.out)


__author__ = 'manitou'
