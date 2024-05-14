import pytest
from selenium import webdriver
from config import URL,RESOLUTION
from random import randint


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

def get_sign_up_data():
    email = f'email'+str(randint(0,1000))+'@mail.ru'
    password = f'12345678'+str(randint(0,1000))
    name = f'Михаил'+str(randint(0,1000))
    return name,email,password