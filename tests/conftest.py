import pytest
from selenium import webdriver
from config import URL,RESOLUTION
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators

def browser_settings():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--window-size={RESOLUTION[0]}, {RESOLUTION[1]}')
    return chrome_options


@pytest.fixture()
def driver():
    chrome = webdriver.Chrome()
    chrome.get(URL)
    yield chrome
    chrome.quit()
