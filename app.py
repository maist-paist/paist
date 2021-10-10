import webview
import os
import sys
import re

from config import config

def resource_path(relative_path): 
    """ Get absolute path to resource, works for dev and for PyInstaller """ 
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))) 
    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    base_path = resource_path("frontend/index.html")
    
    window = webview.create_window(config.name, base_path)
    window.closing += lambda: config.isWindows
    webview.start(gui="edgechromium" if config.isWindows else None)