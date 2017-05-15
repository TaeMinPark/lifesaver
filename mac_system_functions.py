# -*- coding: utf-8 -*-
__author__ = 'Min'
import os
from AppKit import NSWorkspace


def get_running_applications():
    return map(lambda app: app.localizedName(), NSWorkspace.sharedWorkspace().runningApplications())


def get_active_window_name():
    return NSWorkspace.sharedWorkspace().frontmostApplication().localizedName()


def press_save():
    cmd = """osascript -e 'tell application "System Events" to keystroke "s" using {command down}'"""
    os.system(cmd)