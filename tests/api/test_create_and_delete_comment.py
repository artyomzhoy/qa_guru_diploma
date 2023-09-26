import allure

from helper.api.api_requests import post_comment, delete_comment, get_comment
from decouple import config
from jsonschema.validators import validate
from helper.api.schema import load_json_schema
from allure_commons.types import Severity


@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.label('Test Type', 'API')
@allure.title('Создание комментария')
def test_create_comment():
    schema = load_json_schema('create_comment_schema.json')
    image_id = 'REUyCW5'
    comment = 'So cute!'
    access_token = config('ACCESS_TOKEN')
    headers = {'Authorization': f'Bearer {access_token}'}

    with allure.step('Create comment'):
        response = post_comment(headers, image_id, comment)
        comment_id = response.json()['data']['id']

    with allure.step('Assert a results of creating comment'):
        assert response.status_code == 200
        validate(instance=response.json(), schema=schema)

    with allure.step('Check creating comment'):
        response = get_comment(headers, comment_id)

    with allure.step('Assert a results of checking creating comment'):
        assert response.status_code == 200
        assert response.json()['data']['image_id'] == image_id
        assert response.json()['data']['comment'] == comment

    with allure.step('Deleting test data'):
        delete_comment(headers, comment_id)


@allure.tag('api')
@allure.severity(Severity.CRITICAL)
@allure.label('Test Type', 'API')
@allure.title('Удаление комментария')
def test_delete_comment():
    schema = load_json_schema('delete_comment_schema.json')
    image_id = 'REUyCW5'
    comment = 'So cute!'
    access_token = config('ACCESS_TOKEN')
    headers = {'Authorization': f'Bearer {access_token}'}

    with allure.step('Preparing test data'):
        response = post_comment(headers, image_id, comment)
        comment_id = response.json()['data']['id']

    with allure.step('Delete comment'):
        response = delete_comment(headers, comment_id)

    with allure.step('Assert a results of deleting comment'):
        assert response.status_code == 200
        validate(instance=response.json(), schema=schema)

    with allure.step('Check deleting comment'):
        response = get_comment(headers, comment_id)

    with allure.step('Assert a results of checking deleted comment'):
        assert response.status_code == 404
