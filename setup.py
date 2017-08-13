"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup
import sys

APP = 'lifesaver.py'
DATA_FILES = ['resources/icon.png', 'resources/icon.ico']
OPTIONS = {}


if sys.platform == "win32":
    # python setup.py py2exe
    import py2exe

    platform_options = {
        "windows": [
            {
                "script": APP,
                "icon_resources": [(1, "resources/icon.ico")]
            }
        ],
        "zipfile": None,
        "setup_requires": ["py2exe"],
        "options": {
            "py2exe": {
                "compressed": True,
                'packages': ['wx']
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
                "iconfile": "resources/icon.ico",
                'packages': ['wx'],
            }
        }
    }
else:
    platform_options = {
        "scripts": [APP]
    }

setup(
    name="lifesaver",
    description="Save your life by saving your file regularly",
    data_files=DATA_FILES,
    packages=['src'],
    **platform_options
)
