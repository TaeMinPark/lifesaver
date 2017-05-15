# -*- coding: utf-8 -*-
__author__ = 'Min'
import ctypes, os, json
import win32com


def get_exe_by_hwid(hwid):
    process_id = ctypes.c_int()
    ctypes.windll.user32.GetWindowThreadProcessId(hwid, ctypes.byref(process_id))
    MAX_PATH = 260
    PROCESS_TERMINATE = 0x0001
    PROCESS_QUERY_INFORMATION = 0x0400

    process_id= process_id.value
    process = ctypes.windll.Kernel32.OpenProcess(PROCESS_TERMINATE | PROCESS_QUERY_INFORMATION, False, process_id)

    if process:
        imagefile_name = (ctypes.c_char * MAX_PATH)()
        if ctypes.windll.Psapi.GetProcessImageFileNameA(process, imagefile_name, MAX_PATH) > 0:
            exe_name = os.path.basename(imagefile_name.value)

    return exe_name


def get_running_applications():
    running_apps = []
    GW_HWNDNEXT=2
    top_app = ctypes.windll.user32.GetTopWindow(None)

    if not top_app:
        return running_apps
    buf_app = top_app

    while True:
        nxt_app = ctypes.windll.user32.GetWindow(buf_app, GW_HWNDNEXT)
        if not nxt_app:
            break  # No app anymore
        if ctypes.windll.user32.IsWindowVisible(nxt_app):  # Only visible windows
            process_exe_name = get_exe_by_hwid(nxt_app)
            if process_exe_name not in running_apps:  # Only one time
                running_apps.append(process_exe_name)
        buf_app = nxt_app

    return running_apps


def get_active_window_name():
    return get_exe_by_hwid(ctypes.windll.user32.GetForegroundWindow())


def press_save():
    win32com.client.Dispatch("WScript.Shell").SendKeys("^s")


def get_data_storage_path():
    return os.path.join(os.environ['APPDATA'], 'lifesaver')


def is_first_run():
    return os.path.isfile(get_data_storage_path() + '/config.json')


def setup_app_first_run():
    os.makedirs(get_data_storage_path())
    with open(get_data_storage_path() + '/config.json', 'w+') as data_file:
        data = '{"target_apps": [], "run_on_startup": 0}'
        data_file.write(data)


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


def change_run_at_startup_to_config():
    with open(get_data_storage_path() + '/config.json', 'r') as data_file:
        data = json.load(data_file)
    if data['run_on_startup'] == 1:
        data['run_on_startup'] = 0
    else:
        data['run_on_startup'] = 1

    with open(get_data_storage_path() + '/config.json', 'w') as data_file:
        json.dump(data, data_file, indent = 4)


def is_run_at_startup():
    with open(get_data_storage_path() + '/config.json', 'r') as data_file:
        data = json.load(data_file)
    if data['run_on_startup'] == 1:
        return True
    else:
        return False