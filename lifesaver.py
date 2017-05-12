# -*- coding: utf-8 -*-
__author__ = 'Min'

import sys, os, threading, rumps
from AppKit import NSWorkspace


class LifesaverMacStatusBar(rumps.App):
    def __init__(self, title):
        super(LifesaverMacStatusBar, self).__init__(title)
        self.menu = [
            {
                'Target app': self.make_apps_submenu(self.get_running_applications())
            },
            None
        ]
        self.target_processes = []
        self.execute_save_thread()

    def get_active_window_name(self):
        return NSWorkspace.sharedWorkspace().frontmostApplication().localizedName()

    def execute_save_thread(self):
        if self.get_active_window_name() in self.target_processes:
            self.press_save()

        threading.Timer(10, self.execute_save_thread).start()

    def press_save(self):
        cmd = """osascript -e 'tell application "System Events" to keystroke "s" using {command down}'"""
        os.system(cmd)

    def get_running_applications(self):
        return NSWorkspace.sharedWorkspace().runningApplications()

    def make_apps_submenu(self, apps):
        return map(lambda app: rumps.MenuItem(app, callback=self.set_target_app),
                   sorted(map(lambda app: app.localizedName(), apps)))

    def set_target_app(self, sender):
        sender.state = not sender.state
        if sender.state:
            self.target_processes.append(sender.title)
        else:
            self.target_processes.remove(sender.title)

if __name__ == "__main__":

    if sys.platform == "darwin":
        LifesaverMacStatusBar("Saver").run()
    #elif sys.platform == "win32":
        #from windows import LifesaverWindowsStatusBar
        #LifesaverWindowsStatusBar