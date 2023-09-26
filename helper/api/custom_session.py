import curlify
from requests import Session, Response
import allure
from utils import attach


class CustomSession(Session):
    def __init__(self, base_url):
        self.base_url = base_url
        super().__init__()

    def request(self, method, url, **kwargs) -> Response:
        response = super(CustomSession, self).request(method=method, url=self.base_url + url, **kwargs)
        curl = curlify.to_curl(response.request)
        if 'application/json' in curl:
            response_type = response.json()
        else:
            response_type = response.text
        with allure.step(f'{method} {url}'):
            attach.add_response_code(response)
            attach.add_curl(curl)
            if response.content:
                attach.add_response(response_type)
            else:
                attach.add_empty_response()
            return response


project_url = CustomSession('https://api.imgur.com/')
