"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup
import sys

APP = 'lifesaver.py'
DATA_FILES = []
OPTIONS = {}
INCLUDES = ["PySide.QtCore",
            "PySide.QtGui",
            "PySide.QtWebKit",
            "PySide.QtNetwork",
            "PySide.QtXml"]
WIN_DLL_INCLUDE = ["w9xpopen.exe",
                   "msvcr71.dll",
                   "MSVCP90.dll"],

if sys.platform == "win32":
    # python setup.py py2exe
    import py2exe

    platform_options = {
        "windows": [{
                        "script": APP,
                        "icon_resources": [(1, "window_icon.ico")]
                    }],
        "zipfile": None,
        "setup_requires": ["py2exe"],
        "options": {
            "py2exe": {
                "includes": INCLUDES,
                "dll_excludes": WIN_DLL_INCLUDE,
                "compressed": True
            }
        }
    }
elif sys.platform == "darwin":
    # python setup.py py2app
    platform_options = {
        "setup_requires": ['py2app'],
        "app": [APP],
        "options": {
            "py2app": {
                "argv_emulation": True,
                "plist": {
                    'LSUIElement': True,
                },
                'packages': ['rumps'],
                #"includes": INCLUDES,
            }
        }

    }
else:
    platform_options = {
        "scripts": [APP]
    }

setup(
    name="lifesaver",
    description="Save your life by saving everything regularly",
    data_files=DATA_FILES,
    **platform_options
)
