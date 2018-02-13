# -*- coding: utf-8 -*-
import wx

from core.parser_factory import ParserFactory
from runners import get_runner

CONFIG_FILE = './config.json'
parser_factory = ParserFactory()
parser_factory.init_parsers(CONFIG_FILE)
app = wx.App()


class DropTarget(wx.FileDropTarget):
    def __init__(self, window):
        super().__init__()
        self.window = window

    def OnDropFiles(self, x, y, filenames):
        for file in filenames:
            if not file.endswith('.log'):
                self.window.error('File {} does not supported'.format(file))
                continue
            out = file if self.window.replace_check.IsChecked() else self.window.get_output_file()
            if not out:
                return True
            self.window.run_conversion(file, out)
        return True


class ConvFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, id=wx.ID_ANY, title="DBusII log conversion", size=(350, 230), style=wx.DEFAULT_FRAME_STYLE & (~wx.RESIZE_BORDER))
        self.status_bar = self.CreateStatusBar(id=wx.ID_ANY)
        self.layout = wx.BoxSizer(wx.VERTICAL)

        # MENU
        mbar = wx.MenuBar()
        self.menu = wx.Menu()
        open_file_action = self.menu.Append(wx.ID_ANY, '&Open file', 'Open log file')
        make_config_action = self.menu.Append(wx.ID_ANY, '(Re)Make config', 'Make converter configuration')
        exit_action = self.menu.Append(wx.ID_EXIT, 'E&xit', 'Exit program')
        self.Bind(wx.EVT_MENU, self.on_file_open, open_file_action)
        self.Bind(wx.EVT_MENU, self.make_config, make_config_action)
        self.Bind(wx.EVT_MENU, lambda *a: self.Destroy(), exit_action)
        mbar.Append(self.menu, 'Menu')
        self.SetMenuBar(mbar)

        # BODY
        self.drop_target = DropTarget(self)
        self.open_button = wx.Button(self, id=wx.ID_ANY, label='Open file (or drop here)', size=(350, 200), pos=(0, 0))
        self.open_button.Bind(wx.EVT_BUTTON, self.on_file_open)
        self.open_button.SetDropTarget(self.drop_target)
        self.replace_check = wx.CheckBox(self, id=wx.ID_ANY, label="Replace existing file", size=(350, 15), pos=(0, 200))

        # LAYOUT
        #self.layout.Add(self.menu)
        self.layout.Add(self.replace_check, 0, wx.ALL)
        self.layout.Add(self.open_button, 1, wx.ALL|wx.EXPAND)
        self.layout.Fit(self)

    def make_config(self, event):
        pass

    def run_conversion(self, in_, out):
        '''Only for logfiles for now'''
        runner_cls = get_runner('replace' if self.replace_check.IsChecked() else 'simple')
        runner = runner_cls(parser_factory)
        try:
            runner.run(in_, out)
        except Exception as e:
            self.error(str(e))
        else:
            self.info('File converted.')

    def error(self, msg):
        errorDlg = wx.MessageDialog(self, msg, "Error", wx.OK)
        errorDlg.ShowModal()


    def info(self, msg):
        self.status_bar.SetStatusText(msg)


    def get_output_file(self):
        with wx.FileDialog(self, "Save output log file",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            return fileDialog.GetPath()


    def get_input_file(self):
        with wx.FileDialog(self, "Open log file", wildcard="Log files (*.log)|*.log",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            return fileDialog.GetPath()


    def on_file_open(self, event):
        in_ = self.get_input_file()
        if not in_:
            return
        out = in_ if self.replace_check.IsChecked() else self.get_output_file()
        if not out:
            return
        self.run_conversion(in_, out)



if __name__ == '__main__':
    wnd = ConvFrame()
    wnd.Show(True)
    app.MainLoop()


__author__ = 'manitou'
