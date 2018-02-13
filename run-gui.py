# -*- coding: utf-8 -*-
import wx

from core.parser_factory import ParserFactory
from runners import get_runner

CONFIG_FILE = './config.json'
parser_factory = ParserFactory()
parser_factory.init_parsers(CONFIG_FILE)
app = wx.App()


class DropTarget(wx.FileDropTarget):
    def OnDropFiles(self, x, y, filenames):
        for file in filenames:
            out = get_output_file()
            if not out:
                return
            run_conversion(file, out)


def run_conversion(in_, out):
    '''Only for logfiles for now'''
    runner_cls = get_runner('simple')
    runner = runner_cls(parser_factory)
    try:
        runner.run(in_, out)
    except Exception as e:
        errorDlg = wx.MessageDialog(None, str(e), "Error", wx.OK)
        errorDlg.ShowModal()


def get_output_file():
    with wx.FileDialog(None, "Save output log file",
                       style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
        if fileDialog.ShowModal() == wx.ID_CANCEL:
            return
        return fileDialog.GetPath()


def get_input_file():
    with wx.FileDialog(None, "Open log file", wildcard="Log files (*.log)|*.log",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
        if fileDialog.ShowModal() == wx.ID_CANCEL:
            return
        return fileDialog.GetPath()


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
    wnd = wx.Frame(None, wx.ID_ANY, "I'm the title")
    open_button = wx.Button(wnd, wx.ID_ANY, 'Open file')
    open_button.Bind(wx.EVT_BUTTON, on_open)
    drop_target = DropTarget()
    open_button.SetDropTarget(drop_target)
    wnd.Show(True)
    app.MainLoop()


__author__ = 'manitou'
