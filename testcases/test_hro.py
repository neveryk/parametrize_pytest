import pytest
import allure
from testcases.conftest import ten,api_data
class Test_Hro():
    @allure.step('创建客户接口')
    @pytest.mark.parametrize('costomerCity_arr,name,hrContactName,hrContactPhone,cityId,cityName,AreaPath,serverId,serverName,declareUnitId',api_data['test_add_client'])
    def test_add_client(self,costomerCity_arr,name,hrContactName,hrContactPhone,cityId,cityName,AreaPath,serverId,serverName,declareUnitId):
        res=ten.add_client(costomerCity_arr,name,hrContactName,hrContactPhone,cityId,cityName,AreaPath,serverId,serverName,declareUnitId)
        return res