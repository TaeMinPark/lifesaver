# -*- coding: utf-8 -*-
__author__ = 'Min'
import os, json, Quartz
from AppKit import NSWorkspace, NSSearchPathForDirectoriesInDomains


def get_running_applications():
    apps = []
    for app in Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID):
        if app['kCGWindowLayer'] == 0:
            if app['kCGWindowOwnerName'] not in apps:
                apps.append(app['kCGWindowOwnerName'])
    return apps


def get_active_window_name():
    return NSWorkspace.sharedWorkspace().frontmostApplication().localizedName()


def press_save():
    cmd = """osascript -e 'tell application "System Events" to keystroke "s" using {command down}'"""
    os.system(cmd)


def get_data_storage_path():
    return os.path.join(NSSearchPathForDirectoriesInDomains(14, 1, True)[0], 'lifesaver')


def setup_app_first_run():
    os.makedirs(get_data_storage_path())
    with open(get_data_storage_path() + '/config.json', 'w+') as data_file:
        data = '{"target_apps": [], "run_on_startup": 0}'
        data_file.write(data)

    with open(os.path.expanduser('~') + '/Library/LaunchAgents/lifesaver.plist', 'w') as plist_file:
        data = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict><key>Label</key><string>life.saver</string><key>ProgramArguments</key><array><string>/usr/bin/open</string><string>/Applications/lifesaver.app</string></array><key>StandardErrorPath</key><string>/var/log/python_script.error</string><key>RunAtLoad</key><true/></dict></plist>'
        plist_file.write(data)


def change_run_at_startup_to_config():
    with open(get_data_storage_path() + '/config.json', 'r') as data_file:
        data = json.load(data_file)
    if data['run_on_startup'] == 1:
        data['run_on_startup'] = 0
        os.system('launchctl unload ~/Library/LaunchAgents/lifesaver.plist')
    else:
        data['run_on_startup'] = 1
        os.system('launchctl load ~/Library/LaunchAgents/lifesaver.plist')
    with open(get_data_storage_path() + '/config.json', 'w') as data_file:
        json.dump(data, data_file, indent = 4)