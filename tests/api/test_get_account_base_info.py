import allure

from helper.api.api_requests import get_account_base_info
from jsonschema import validate
from helper.api.schema import load_json_schema
from decouple import config
from allure_commons.types import Severity


@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.label('Test Type', 'API')
@allure.title('Получение информации о аккаунте')
def test_get_account_base_info():
    schema = load_json_schema('account_base_schema.json')

    userid = config('CLIENT_ID')
    username = config('ACCOUNT_USERNAME')
    headers = {'Authorization': f'Client-ID {userid}'}

    with allure.step('Make a request'):
        response = get_account_base_info(username, headers)

    with allure.step('Assert a results'):
        assert response.status_code == 200
        assert response.json()['data']['url'] == username
        validate(instance=response.json(), schema=schema)
