import allure

from helper.api.api_requests import follow_tag, unfollow_tag, get_tag_info
from decouple import config
from jsonschema.validators import validate
from helper.api.data_generation import tag
from helper.api.schema import load_json_schema
from allure_commons.types import Severity


@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.label('Test Type', 'API')
@allure.title('Подписка на тэг')
def test_following_tag():
    followed_tag = tag()
    schema = load_json_schema('follow_tag_schema.json')
    access_token = config('ACCESS_TOKEN')
    headers = {'Authorization': f'Bearer {access_token}'}

    with allure.step('Follow tag'):
        response = follow_tag(followed_tag, headers)

    with allure.step('Assert a results of following tag'):
        assert response.status_code == 200
        validate(instance=response.json(), schema=schema)

    with allure.step('Check following tag'):
        response = get_tag_info(followed_tag, headers)

    with allure.step('Assert a results of check tag_follow'):
        assert response.status_code == 200
        assert response.json()['data']['tag_follow'] == {'status': True}

    with allure.step('Deleting test data'):
        unfollow_tag(followed_tag, headers)


@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.label('Test Type', 'API')
@allure.title('Отписка от тэга')
def test_unfollowing_tag():
    followed_tag = tag()
    schema = load_json_schema('unfollow_tag_schema.json')
    access_token = config('ACCESS_TOKEN')
    headers = {'Authorization': f'Bearer {access_token}'}

    with allure.step('Preparing test data'):
        follow_tag(followed_tag, headers)

    with allure.step('Unfollow tag'):
        response = unfollow_tag(followed_tag, headers)

    with allure.step('Assert a results of unfollowing tag'):
        assert response.status_code == 200
        validate(instance=response.json(), schema=schema)

    with allure.step('Check unfollowing tag'):
        response = get_tag_info(followed_tag, headers)

    with allure.step('Assert a results of check tag_follow'):
        assert response.status_code == 200
        assert response.json()['data']['tag_follow'] == {'status': False}
