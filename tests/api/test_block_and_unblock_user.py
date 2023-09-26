import allure

from helper.api.api_requests import get_block_list, unblock_user, block_user
from decouple import config
from allure_commons.types import Severity
from jsonschema.validators import validate

from helper.api.data_generation import user
from helper.api.schema import load_json_schema


@allure.tag('api')
@allure.severity(Severity.BLOCKER)
@allure.label('Test Type', 'API')
@allure.title('Блокировка пользователя')
def test_block_user():
    blocked_user = user()
    schema = load_json_schema('block_list_schema.json')
    access_token = config('ACCESS_TOKEN')
    headers = {'Authorization': f'Bearer {access_token}'}

    with allure.step('Make a block'):
        response = block_user(blocked_user, headers)

    with allure.step('Assert a results of block'):
        assert response.status_code == 201

    with allure.step('Checking block list'):
        response = get_block_list(headers)
        print(response.content)

    with allure.step('Assert a result of check'):
        assert response.status_code == 200
        assert response.json()['data']['items'][0] == {"url": f'{blocked_user}'}
        validate(instance=response.json(), schema=schema)

    with allure.step('Deleting test data'):
        unblock_user(blocked_user, headers)


@allure.tag('api')
@allure.severity(Severity.BLOCKER)
@allure.label('Test Type', 'API')
@allure.title('Разблокировка пользователя')
def test_unblock_user():
    blocked_user = user()
    schema = load_json_schema('block_list_schema.json')
    access_token = config('ACCESS_TOKEN')
    headers = {'Authorization': f'Bearer {access_token}'}

    with allure.step('Preparing test data'):
        block_user(blocked_user, headers)

    with allure.step('Make a unblock'):
        response = unblock_user(blocked_user, headers)

    with allure.step('Assert a results of unblock'):
        assert response.status_code == 204

    with allure.step('Checking block list'):
        response = get_block_list(headers)

    with allure.step('Assert a result of check'):
        assert response.status_code == 200
        assert response.json()['data']['items'] == []
        validate(instance=response.json(), schema=schema)
