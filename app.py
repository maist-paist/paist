import webview
import os
import sys
import re

from config import config

def resource_path(relative_path): 
    """ Get absolute path to resource, works for dev and for PyInstaller """ 
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__))) 
    return os.path.join(base_path, relative_path)


def load_html(window):
    base_path = resource_path("frontend")
    print(base_path)
    css = []
    js = []
    index = ""
    def read_css(css_file_path):
        try:
            with open(base_path + css_file_path) as f_obj:
                css = f_obj.read()
        except Exception as error:
            print("Error opening .css file.")
            print(error, type(error))
        else:
            return css

    def read_js(js_file_path):
        try:
            with open(base_path + js_file_path) as f_obj:
                js = f_obj.read()
        except Exception as error:
            print("Error opening .js file.")
            print(error, type(error))
        else:
            return js

    html = ""
    
    css_pattern = re.compile('<link.*>')
    js_pattern = re.compile('<script.*>')

    with open(os.path.join(base_path, 'index.html')) as f_obj:
        lines = f_obj.read().replace('>', '>\n').split('\n')

        js_input = False
        for line in lines:
            if js_input:
                js_input = False
                continue

            match_css = css_pattern.match(line)
            if match_css is not None:
                link_parts = line.split(' ')
                for part in link_parts:
                    if 'href' in part:
                        if 'http' in part:
                            html+= line
                        else:
                            css_file_path = part.replace('href="', '').replace('">', '').replace('"', '').replace('\n', '')
                            css = read_css(css_file_path)
                            html += '<style>' + css + '</style>'
                        
            else:
                match_js = js_pattern.match(line)
                if match_js is not None:
                    if 'src' in line:
                        script_parts = line.split(' ')
                        for part in script_parts:
                            if 'src' in part:
                                if 'http' in part:
                                    html+= line
                                else:
                                    js_file_path = part.replace('src="', '').replace('">', '').replace('"', '').replace('\n', '')
                                    js = read_js(js_file_path)
                                    html += '<script>' + js + '</script>'
                                    js_input = True
                    else:
                        html+= line
                else:
                    html+= line
                
    window.load_html(html)

if __name__ == "__main__":
    window = webview.create_window(config.name)
    window.closing += lambda: False
    webview.start(load_html, (window))