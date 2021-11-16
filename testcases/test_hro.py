import pytest
import allure
from testcases.conftest import ten,api_data
class Test_Hro():
    @allure.step('创建客户接口')
    @pytest.mark.parametrize('costomerCity_arr,name,hrContactName,hrContactPhone,cityId,cityName,AreaPath,serverId,serverName,declareUnitId',api_data['test_add_client'])
    def test_add_client(self,costomerCity_arr,name,hrContactName,hrContactPhone,cityId,cityName,AreaPath,serverId,serverName,declareUnitId):
        res=ten.add_client(costomerCity_arr,name,hrContactName,hrContactPhone,cityId,cityName,AreaPath,serverId,serverName,declareUnitId)
        return res

    # @allure.step('设置默认值')
    # @pytest.mark.parametrize("customerId,category,projectId",api_data["test_add_default"])
    # def test_service_defu(self,customerId,category,projectId):
    #     res=ten.add_default(customerId,category,projectId)
    #     return res
