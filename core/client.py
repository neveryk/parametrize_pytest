import requests
import os
import allure
import logging
from public import config

BASE_PATH=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

class Client:
    def __init__(self,host,**kwargs):
        self.host=host
        self.session=requests.session()

    def post(self,url,jsondata=None,**kwargs):
        res=self.session.post(self.host+url,json=jsondata,**kwargs)
        allure.attach(res.text, 'response-data', allure.attachment_type.TEXT)
        re_j=res.json()
        try:
            if re_j["message"] == '登录成功！':
                return re_j
        except Exception as e:
            logging.basicConfig(filename=config.src_path + '/log/syserror.log', level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)

    def get(self,url,jsondata=None,**kwargs):
        res = self.session.get(self.host + url, json=jsondata, **kwargs)
        allure.attach(res.text, 'response-data', allure.attachment_type.TEXT)
        re_j=res.json()
        try:
            if re_j["message"] == '登录成功！':
                return re_j
        except Exception as e:
            logging.basicConfig(filename=config.src_path + '/log/syserror.log', level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)

    def post_data(self,url,jsondata=None,**kwargs):
        res=self.session.post(self.host+url,files=jsondata,**kwargs)
        allure.attach(res.text, 'response-data', allure.attachment_type.TEXT)
        re_j = res.json()
        try:
            if re_j["message"] == '登录成功！':
                return res
        except Exception as e:
            logging.basicConfig(filename=config.src_path + '/log/syserror.log', level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)