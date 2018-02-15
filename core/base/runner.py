# -*- coding: utf-8 -*-

# implements task which will perform all work


class BaseRunner(object):
    name = None
    producer = None
    consumer = None
    parser_factory = None

    def __init__(self, parser_factory):
        self.parser_factory = parser_factory

    def run(self, in_, out):
        '''Runs conversion'''
        with self.producer(out) as producer:
            with self.consumer(in_) as consumer:
                for entry in consumer.input():
                    parser = self.parser_factory.get(entry.id)
                    container = parser.process(entry)
                    try:
                        producer.output(container)
                    except Exception as e:
                        print('Exception in row:', container.src_data)
                        raise


__author__ = 'manitou'
