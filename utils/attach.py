import json
import allure
from allure_commons.types import AttachmentType


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='Screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    log = ''.join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'Browser logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'Page source', AttachmentType.HTML, '.html')


def add_video(browser):
    video_url = 'https://selenoid.autotests.cloud/video/' + browser.driver.session_id + '.mp4'
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'Video_' + browser.driver.session_id, AttachmentType.HTML, '.html')


def add_response_code(response):
    allure.attach(
        body=f'Status code: {response.status_code}',
        name='Status code',
        attachment_type=AttachmentType.TEXT,
        extension='txt'
    )


def add_curl(curl):
    allure.attach(
        body=curl.encode('utf8'),
        name='Curl',
        attachment_type=AttachmentType.TEXT,
        extension='txt'
    )


def add_response(response_type):
    allure.attach(
        body=json.loads(json.dumps(response_type)),
        name='Response JSON',
        attachment_type=AttachmentType.JSON,
        extension='json')


def add_empty_response():
    allure.attach(
        body='Empty response',
        name='Empty response',
        attachment_type=AttachmentType.TEXT,
        extension='txt')
