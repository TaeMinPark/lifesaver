# -*- coding: utf-8 -*-
__author__ = 'Min'
import sys

if sys.platform == 'win32':
    import windows_system_functions as win_sys_funcs
elif sys.platform == 'darwin':
    import mac_system_functions as mac_sys_funcs


def run_by_platform(win_func, mac_func, *args):
    if sys.platform == 'win32':
        return win_func(*args)
    elif sys.platform == 'darwin':
        return mac_func(*args)


def get_active_window_name():
    if sys.platform == 'win32':
        return win_sys_funcs.get_active_window_name()
    elif sys.platform == 'darwin':
        return mac_sys_funcs.get_active_window_name()


def get_running_applications():
    if sys.platform == 'win32':
        return sorted(win_sys_funcs.get_running_applications())
    elif sys.platform == 'darwin':
        return sorted(mac_sys_funcs.get_running_applications())


def press_save():
    if sys.platform == 'win32':
        win_sys_funcs.press_save()
    elif sys.platform == 'darwin':
        mac_sys_funcs.press_save()


def get_data_storage_path():
    if sys.platform == 'win32':
        return win_sys_funcs.get_data_storage_path()
    elif sys.platform == 'darwin':
        return mac_sys_funcs.get_data_storage_path()


def is_first_run():
    if sys.platform == 'win32':
        return not win_sys_funcs.is_first_run()
    elif sys.platform == 'darwin':
        return not mac_sys_funcs.is_first_run()


def setup_app_first_run():
    if sys.platform == 'win32':
        win_sys_funcs.setup_app_first_run()
    elif sys.platform == 'darwin':
        mac_sys_funcs.setup_app_first_run()


def get_targetapps_from_config():
    if sys.platform == 'win32':
        return win_sys_funcs.get_targetapps_from_config()
    elif sys.platform == 'darwin':
        return mac_sys_funcs.get_targetapps_from_config()


def update_targetapps_to_config(target_apps):
    if sys.platform == 'win32':
        win_sys_funcs.update_targetapps_to_config(target_apps)
    elif sys.platform == 'darwin':
        mac_sys_funcs.update_targetapps_to_config(target_apps)


def is_run_at_startup():
    if sys.platform == 'win32':
        return win_sys_funcs.is_run_at_startup()
    elif sys.platform == 'darwin':
        return mac_sys_funcs.is_run_at_startup()


def change_run_at_startup_to_config(event):
    if sys.platform == 'win32':
        win_sys_funcs.change_run_at_startup_to_config()
    elif sys.platform == 'darwin':
        mac_sys_funcs.change_run_at_startup_to_config()