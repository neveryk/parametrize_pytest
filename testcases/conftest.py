import pytest
import yaml
import os
from common.read_data import data_yaml
import logging
from api.tenant import Tenant
import allure
from functools import wraps

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, 'config', 'setting.ini')


def get_data(yaml_file_name):
    data_file_path = os.path.join(BASE_PATH, 'data', yaml_file_name)
    yaml_data = data_yaml.load_yaml(data_file_path)
    return yaml_data



api_data = get_data('api_data.yml')
print(api_data)

HOST = data_yaml.load_ini(data_file_path)['host']['BASEURL']
tenant = Tenant(HOST)
