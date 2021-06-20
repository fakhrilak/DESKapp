import time
import requests
import win32serviceutil
from pathlib import Path
import sys
from SMWinservice import SMWinservice
import sys

class PythonCornerExample(SMWinservice):
    _svc_name_ = "test123"
    _svc_display_name_ = "hello world"
    _svc_description_ = "That's a great winservice! :)"

    def start(self):
        self.isrunning = True

    def stop(self):
        self.isrunning = False

    def main(self):
        while True:
            requests.get("http://192.168.10.120:3003/komputer?page=0&limit=1")
            time.sleep(5)
if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PythonCornerExample)
        




    
