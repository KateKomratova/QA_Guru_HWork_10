import pytest
import os
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from utils import attach

# Загрузка переменных окружения из .env
@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='128.0'
    )

@pytest.fixture(scope="function")
def browser_conf(request):
    browser_version = request.config.getoption('--browser_version')
    options = Options()
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    # Получаем данные из переменных окружения
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    # Создание удалённого драйвера
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options)

    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()