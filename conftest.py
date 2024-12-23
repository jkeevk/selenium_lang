from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, en, fr, es etc.")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    print("\nstart chrome browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)    
    yield browser
    print("\nquit browser..")
    browser.quit()
    
    