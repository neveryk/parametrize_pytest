import requests
import os
import json
import allure
BASE_PATH=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

class Client:
    def __init__(self,host,**kwargs):
        self.host=host
        self.session=requests.session()

    def post(self,url,jsondata=None,**kwargs):
