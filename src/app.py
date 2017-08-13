# -*- coding: utf-8 -*-
__author__ = 'Min'
import wx, wx.adv, threading, system_functions
from functools import partial
TRAY_TOOLTIP = 'LifeSaver'
TRAY_ICON = 'icon.png'


class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self, frame):
        self.frame = frame
        super(TaskBarIcon, self).__init__()
        self.set_icon(TRAY_ICON)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)  # When left key pressed
        self.target_processes = system_functions.get_targetapps_from_config()
        self.save_thread = None  # Save thread
        self.execute_save_thread()  # Starting save thread
        self.is_run_at_startup = system_functions.is_run_at_startup()

    def CreatePopupMenu(self):
        main_menu = wx.Menu()
        targetapp_menu = self.make_targetapp_menu()  # Creates target apps menu

        main_menu.AppendMenu(100, "Target App", targetapp_menu)  # Add target apps menu to main menu
        main_menu.AppendSeparator()
        run_at_startup_menu = main_menu.Append(-1, 'Run at startup', '', wx.ITEM_CHECK)
        self.Bind(wx.EVT_MENU, system_functions.change_run_at_startup_to_config,
                  id = run_at_startup_menu.GetId())

        if system_functions.is_run_at_startup():
            main_menu.Check(run_at_startup_menu.GetId(), True)

        exit_menu = main_menu.Append(-1, 'Exit')
        self.Bind(wx.EVT_MENU, self.on_exit, id = exit_menu.GetId())

        return main_menu

    def make_targetapp_menu(self):
        targetapp_menu = wx.Menu()
        for app in system_functions.get_running_applications():
            app_menu = targetapp_menu.Append(wx.NewId(), app, '', wx.ITEM_CHECK)
            self.Bind(wx.EVT_MENU, partial(self.set_target_app, app), id = app_menu.GetId())
            if app in self.target_processes:
                targetapp_menu.Check(app_menu.GetId(), True)

        return targetapp_menu

    def set_icon(self, path):
        icon = wx.Icon(wx.Bitmap(path))
        self.SetIcon(icon, TRAY_TOOLTIP)

    def on_left_down(self, event):
        self.CreatePopupMenu()  # Create menu on left mouse down

    def on_exit(self, event):
        wx.CallAfter(self.Destroy)  # destroy Wx
        self.frame.Close()  # Close WX frame
        self.save_thread.cancel()  # Stops thread

    def set_target_app(self, name, event):
        if name in self.target_processes:
            self.target_processes.remove(name)
        else:
            self.target_processes.append(name)

        system_functions.update_targetapps_to_config(self.target_processes)

    def execute_save_thread(self):
        if system_functions.get_active_window_name() in self.target_processes: system_functions.press_save()
        self.save_thread = threading.Timer(10, self.execute_save_thread)
        self.save_thread.start()


class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(None)
        self.SetTopWindow(frame)
        TaskBarIcon(frame)
        return True


def main():
    if system_functions.is_first_run(): system_functions.setup_app_first_run()  # Setup app when it's first run
    app = App(False)
    app.MainLoop()


if __name__ == '__main__':
    main()