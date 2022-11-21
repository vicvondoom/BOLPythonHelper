import requests
from requests.auth import HTTPBasicAuth
import json
import datetime
import socket
import traceback
import os
import platform
import urllib3

from enum import Enum

class Languages(Enum):
    NotDefined = 0
    CSharp = 1
    Java = 2
    Python = 3
    Php = 4
    C = 5
    Cplusplus = 6 
    VB6 = 7
    VBNet = 8
    Javascript = 9 
    Swift = 10 
    Ruby = 11
    Perl = 12
    Delphi = 13


class AppTypes(Enum):
    NotDefined = 0
    Mobile = 1
    WebApp = 2
    Desktop = 3
    IoT = 4
    WepApi = 5
    Console = 6


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
        self.BugDate = datetime.datetime.now

        self.Routine= ""
        self.OS= ""
        self.OSVersion= ""

        self.Language = Languages.NotDefined
        self.AppType = AppTypes.NotDefined

        self.Things = {}

class BOLHelper(object):
    """description of class"""
    __instance = None
    __username = ""
    __password = ""
    __appname = ""
    __appversion = ""
    __apptype = AppTypes.NotDefined
    __language = Languages.NotDefined


    @staticmethod 
    def getInstance():
        return BOLHelper.getInstance(BOLHelper.__username, BOLHelper.__password)

    @staticmethod 
    def getInstance():
        return


    @staticmethod 
    def initInstance(username, password, 
                     appName, appVersion, 
                     appType = AppTypes.NotDefined,
                     language = Languages.NotDefined):
        """ Static access method. """
        
        if username != "" and password != "" and appName != "" and appVersion != "":
            BOLHelper.__Instance()
            BOLHelper.__instance.__username = username
            BOLHelper.__password = password
            BOLHelper.__instance.__appname = appName
            BOLHelper.__instance.__appversion = appVersion
            BOLHelper.__instance.__apptype = appType
            BOLHelper.__instance.__language = language
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
        url = "https://api.bugsonline.biz/api/send"
        headers={'Content-type':'application/json', 'Accept':'application/json'}

        b = BOLBug()
        # b.AppName = "main.py"
        # b.AppVersion = "1.0" # ther is no version of a python script
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
