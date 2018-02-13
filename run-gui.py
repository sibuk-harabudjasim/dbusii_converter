# -*- coding: utf-8 -*-
import tkinter
from tkinter.filedialog import LoadFileDialog, SaveFileDialog

from core.parser_factory import ParserFactory
from runners import get_runner

CONFIG_FILE = './config.json'
parser_factory = ParserFactory()
parser_factory.init_parsers(CONFIG_FILE)


def run_conversion(in_, out):
    '''Only for logfiles for now'''
    runner_cls = get_runner('simple')
    runner = runner_cls(parser_factory)
    runner.run(in_, out)


def get_input_file():
    d = LoadFileDialog(root)
    file = d.go('.', '*.log,*.txt')
    if file == '':
        return
    return file


def get_output_file():
    d = SaveFileDialog(root)
    file = d.go('.')
    if file == '':
        return
    return file


def on_drop(*args, **kwargs):
    print('drop', args, kwargs)


def on_open(event):
    in_ = get_input_file()
    if not in_:
        return
    out = get_output_file()
    if not out:
        return
    run_conversion(in_, out)


if __name__ == '__main__':
    root = tkinter.Tk()
    root.resizable(0, 0)
    root.geometry('{}x{}'.format(300, 200))
    open_button = tkinter.Button(root, text='Open logfile')
    open_button.bind("<Button-1>", on_open)
    open_button.pack(fill=tkinter.BOTH, expand=1)
    root.mainloop()


__author__ = 'manitou'
