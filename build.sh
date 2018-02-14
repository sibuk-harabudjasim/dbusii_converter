#!/bin/bash

pyinstaller -n dbus_conv -y --add-data "config.json;." -w run-gui.py


