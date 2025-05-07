import pytest
from selene import browser
from utils import attach

@pytest.fixture(scope="function")
def browser_conf():
    print("\nSetting up browser configuration...")
    browser.config.driver_name = 'edge'
    browser.config.timeout = 10
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'
    yield
    print("\nTearing down browser...")
    browser.quit()

attach.add_screenshot(browser)
attach.add_logs(browser)
attach.add_html(browser)
attach.add_video(browser)