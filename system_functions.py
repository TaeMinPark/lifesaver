# -*- coding: utf-8 -*-
__author__ = 'Min'
import sys, json, os

if sys.platform == 'win32':
    import windows.system_functions as win_sys_funcs
elif sys.platform == 'darwin':
    import mac.system_functions as mac_sys_funcs


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
    return not os.path.isfile(get_data_storage_path() + '/config.json')


def setup_app_first_run():
    if sys.platform == 'win32':
        win_sys_funcs.setup_app_first_run()
    elif sys.platform == 'darwin':
        mac_sys_funcs.setup_app_first_run()


def get_targetapps_from_config():
    with open(get_data_storage_path() + '/config.json', 'r') as data_file:
        data = json.load(data_file)
    return data['target_apps']


def update_targetapps_to_config(target_apps):
    with open(get_data_storage_path() + '/config.json', 'r') as data_file:
        data = json.load(data_file)
    data['target_apps'] = target_apps

    with open(get_data_storage_path() + '/config.json', 'w') as data_file:
        json.dump(data, data_file, indent = 4)


def is_run_at_startup():
    with open(get_data_storage_path() + '/config.json', 'r') as data_file:
        data = json.load(data_file)
    if data['run_on_startup'] == 1:
        return True
    else:
        return False


def change_run_at_startup_to_config(event):
    if sys.platform == 'win32':
        win_sys_funcs.change_run_at_startup_to_config()
    elif sys.platform == 'darwin':
        mac_sys_funcs.change_run_at_startup_to_config()