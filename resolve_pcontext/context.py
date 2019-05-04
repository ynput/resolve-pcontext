"""
Classes:
    - parent Context class
    - child Context class

"""
import os
import pathlib

class Context(object):
    """main class with ability to load plugins"""

    _data = dict()
    _plugins = list()

    def __init__(self):
        self.data = self._data

    def plugins(self, plugins_path):

        for p in os.listdir(plugins_path):
            plugin_file = os.path.basename(p)
            self._plugins.append(plugin_file)


class NewContext(Context):
    """main class with ability to load plugins"""

    _clips = list()

    def __init__(self):
        self.clips = self._clips
