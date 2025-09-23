import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--user_languages', action='store', default=None,
                     help="Choose user languages: en/ru/es.....(etc)")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("--user_languages")
    browser_name = request.config.getoption("--browser_name")
    
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language}
        )
        browser = webdriver.Chrome(options=options)
        
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=options)
    
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")
    
    browser.implicitly_wait(10)
    browser.user_language = user_language
    
    yield browser
    time.sleep(7)
    browser.quit()

