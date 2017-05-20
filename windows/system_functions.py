# -*- coding: utf-8 -*-
__author__ = 'Min'
import ctypes, os, json, time
from ctype_classes import KeyboardInput, Input
from ctypes import wintypes


def get_exe_by_hwid(hwid):
    exe_name = ""
    process_id = ctypes.c_int()
    ctypes.windll.user32.GetWindowThreadProcessId(hwid, ctypes.byref(process_id))
    max_path = 260

    process_terminate = 0x0001
    process_query_info = 0x0400

    process_id = process_id.value
    process = ctypes.windll.Kernel32.OpenProcess(process_terminate | process_query_info, False, process_id)

    if process:
        imagefile_name = (ctypes.c_char * max_path)()
        if ctypes.windll.Psapi.GetProcessImageFileNameA(process, imagefile_name, max_path) > 0:
            exe_name = os.path.basename(imagefile_name.value)

    return exe_name


def get_running_applications():
    running_apps = []
    get_window_next = 2
    top_app = ctypes.windll.user32.GetTopWindow(None)

    if not top_app:
        return running_apps
    buf_app = top_app

    while True:
        nxt_app = ctypes.windll.user32.GetWindow(buf_app, get_window_next)
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


def get_data_storage_path():
    return os.path.join(os.environ['APPDATA'], 'lifesaver')


def setup_app_first_run():
    os.makedirs(get_data_storage_path())
    with open(get_data_storage_path() + '/config.json', 'w+') as data_file:
        data = '{"target_apps": [], "run_on_startup": 0}'
        data_file.write(data)


def press_key(key_code_hex):
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    ctypes.wintypes.ULONG_PTR = ctypes.wintypes.WPARAM
    x = Input(type = 1,  # 1 is Keyboard input
              ki=KeyboardInput(wVk=key_code_hex))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def release_key(key_code_hex):
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    wintypes.ULONG_PTR = wintypes.WPARAM
    x = Input(type=1,  # 1 is Keyboard input
              ki=KeyboardInput(wVk=key_code_hex, dwFlags=0x0002))  # 0x0002 is KeyUp
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def press_save():
    press_key(0X11)  # Ctrl Key
    press_key(0x53)  # S Key
    time.sleep(0.1)
    release_key(0X11)
    release_key(0x53)


def change_run_at_startup_to_config():
    with open(get_data_storage_path() + '/config.json', 'r') as data_file:
        data = json.load(data_file)
    if data['run_on_startup'] == 1:
        data['run_on_startup'] = 0
    else:
        data['run_on_startup'] = 1

    with open(get_data_storage_path() + '/config.json', 'w') as data_file:
        json.dump(data, data_file, indent = 4)