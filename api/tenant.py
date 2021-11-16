from core.client import Client
import allure
import json
import logging
from public import config
from common.url_Splicing import ur
class Tenant(Client):
    def __init__(self,host,**kwargs):
        super(Tenant, self).__init__(host,**kwargs)

    def get_login(self):
        data = {'UserName': 'admin1', 'Password': 'mmkj201509'}
        data1 = json.dumps(data, ensure_ascii=False)
        header = {"Content-Type": "application/json; charset=utf-8"}
        res = self.post('/api/account/login', jsondata=data1, headers=header)
        res_j = res.json()
        try:
            token = res_j["data"]["access_token"]
            header = {"Content-Type": "application/json; charset=utf-8",
                      "Authorization": "Bearer " + token
                      }
            return header
        except Exception as e:
            logging.basicConfig(filename=config.src_path + '/log/syserror.log', level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)

    def add_client(self,costomerCity_arr,name,hrContactName,hrContactPhone,cityId,cityName,AreaPath,serverId,serverName,declareUnitId):
        header=self.get_login()
        # data={"costomerCity_arr": costomerCity_arr, "id": "",
        #  "name": name, "code": "", "superCompanyId": "", "superCompanyName": "", "status": "1", "type": "1",
        #  "category": "", "categoryName": "", "character": "", "characterName": "", "hrContactName": hrContactName,
        #  "hrContactPhone": hrContactPhone, "hrContactEmail": "", "inChargeContacName": "", "inChargeContacPhone": "",
        #  "inChargeContacTitle": "", "phone": "", "email": "", "webSite": "", "postCode": "",
        #  "cityId": cityId, "cityName": cityName,
        #  "AreaPath": AreaPath, "address": "",
        #  "serverId": serverId, "serverName": serverName, "deptCode": "", "financeCode": "",
        #  "declareUnitId": declareUnitId, "categoriesID": [], "invoiceManner": 0,
        #  "categoriesName": "", "categoriesInfo": [], "payDeadLineDayType": "0", "payDeadLineDay": 1,
        #  "isForthwithInvoiceNo": "false", "remarks": "", "signingCompanyId": "", "departmentId": "", "regionId": "",
        #  "salesInfo": [], "description": "", "rowversion": ""}
        # data1=json.dumps(data,ensure_ascii=False)
        # return self.post('/api/Customer/PostCustomer',jsondata=data1.encode(),headers=header)

    def add_default(self,customerId,category,projectId):
        header=self.get_login()
        url_data={
            "customerId":customerId,
            "category":category,
            "projectId":projectId
        }
        data=ur.url_jia(url_data)
        return self.get('/api/InsureProject/BindCustomer' + data, headers=header),self.get('/api/InsureProject/SetDefault' + data, headers=header)