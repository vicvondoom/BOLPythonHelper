import requests
from requests.auth import HTTPBasicAuth
import json
import datetime
import socket
import traceback
import os
import platform
import urllib3

class BOLBug(object):
    """class that represent a bug"""

    def __init__(self):
        self.AppName = ""
        self.AppVersion= ""
        self.MachineName= ""
        self.Token= ""
        self.ErrNumber= 0
        self.Description= ""
        self.StackTrace= ""
        self.Routine= ""
        self.OS= ""
        self.OSVersion= ""

class BOLHelper(object):
    """description of class"""
    __instance = None
    __username = ""
    __password = ""

    @staticmethod 
    def getInstance():
        return BOLHelper.getInstance(BOLHelper.__username, BOLHelper.__password)

    @staticmethod 
    def getInstance(username, password):
        """ Static access method. """

        if username != "" and password != "":
            BOLHelper.__Instance()
            BOLHelper.__instance.__username = username
            BOLHelper.__password = password
            return BOLHelper.__Instance()
        else:
            raise Exception('Username and Password cannot be '' or null!')

    @staticmethod
    def __Instance():
        if BOLHelper.__instance == None:
            BOLHelper()
        return BOLHelper.__instance

    def __init__(self):
      """ Virtually private constructor. """
      if BOLHelper.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         BOLHelper.__instance = self

    def Send(self, ex):
        # url = "https://localhost:44342/api/send"
        url = "https://api.bugsonline.biz/api/send"
        headers={'Content-type':'application/json', 'Accept':'application/json'}

        b = BOLBug()
        b.AppName = "main.py"
        b.AppVersion = "1.0" # ther is no version of a python script
        b.MachineName = socket.gethostname()
        b.ErrNumber = 0 #there is no errnumber in python..
        b.Description = ex
        b.StackTrace = traceback.format_exc()
        b.OS = platform.system()
        b.OSVersion = platform.release()


        try:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            c = json.dumps(b.__dict__, default=str)
            resp = requests.post(url,auth=HTTPBasicAuth(BOLHelper.__instance.__username, BOLHelper.__instance.__password), verify=False, headers=headers, data = c)
            print(resp.text)
        except Exception as ex:
            print("ERROR: " + ex)
            return ex
