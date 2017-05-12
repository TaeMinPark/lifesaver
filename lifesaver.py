# -*- coding: utf-8 -*-
__author__ = 'Min'
import sys


if __name__ == "__main__":
    try:
        if sys.platform == "darwin":
            from mac import LifesaverMacStatusBar
            LifesaverMacStatusBar("Saver").run()
        elif sys.platform == "win32":
            from windows import LifesaverWindowsStatusBar
            LifesaverWindowsStatusBar
    except Exception as ex:
        print(str(ex))