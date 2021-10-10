"""
Run PAIST while developing
:author Chanwoo Gwon, YonseiUniv. Researcher, since 2020.05. ~
:Date 2021.09.29
"""
import subprocess
import webview
import threading
import http.client
import os
from backend.api import Api

from config import config

app_proc = None

def start_react():
    global app_proc
    app_proc = subprocess.Popen(["npm", "run", "start"], cwd="{0}/ReactJS".format(os.path.abspath("./")), shell=config.isWindows)

def end_react():
    global app_proc
    app_proc.terminate()
    return config.isWindows
    
app_start = threading.Thread(target=start_react)
app_start.start()

while True:
    try :
        conn = http.client.HTTPConnection("localhost:{0}".format(config.reactJSDevWebPort))
        conn.request("GET", "/")
        r1 = conn.getresponse()
        print(r1.status, r1.reason)
        if r1.status == 200:
            break
    except :
        pass

print("web view starting...")
windows = webview.create_window(config.name, url="http://localhost:{0}".format(config.reactJSDevWebPort), js_api=Api())
windows.closing += end_react
webview.start(debug=True, gui="edgechromium" if config.isWindows else None)
