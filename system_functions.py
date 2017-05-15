# -*- coding: utf-8 -*-
__author__ = 'Min'
import windows_system_functions, mac_system_functions, sys


def get_active_window_name():
    if sys.platform == 'win32':
        return windows_system_functions.get_active_window_name()
    elif sys.platform == 'darwin':
        return mac_system_functions.get_active_window_name()


def get_running_applications():
    if sys.platform == 'win32':
        return sorted(windows_system_functions.get_running_applications())
    elif sys.platform == 'darwin':
        return sorted(mac_system_functions.get_active_window_name())


def press_save():
    if sys.platform == 'win32':
        windows_system_functions.press_save()
    elif sys.platform == 'darwin':
        mac_system_functions.press_save()