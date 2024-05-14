from config import URL
from locators import StellarBurgersLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestStellarBurgersConstructorPage():

    def test_click_on_sandwich_button(self, driver):
       driver.get(f'{URL}')

       driver.find_element(*StellarBurgersLocators.ENTER_BUTTON_MAIN_PAGE).click()

       driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_MAIN_PAGE).send_keys("MikhailShemakhanskiy8111@yandex.ru")

       driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_MAIN_PAGE).send_keys("1234567")

       driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()

       WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

       driver.find_element(*StellarBurgersLocators.SANDWICH_SAUCE_BUTTON).click()
       WebDriverWait(driver, 10)
       sandwich_button = driver.find_element(*StellarBurgersLocators.SANDWICH_BUTTON)
       sandwich_button.click()
       WebDriverWait(driver, 10)

       assert sandwich_button.get_attribute('class') == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"


    def test_click_on_souce_button(self, driver):
       driver.get(f'{URL}')

       driver.find_element(*StellarBurgersLocators.ENTER_BUTTON_MAIN_PAGE).click()

       driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_MAIN_PAGE).send_keys("MikhailShemakhanskiy8111@yandex.ru")

       driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_MAIN_PAGE).send_keys("1234567")

       driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()

       WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

       sandwich_souce_button = driver.find_element(*StellarBurgersLocators.SANDWICH_SAUCE_BUTTON)
       sandwich_souce_button.click()
       WebDriverWait(driver, 10)

       assert sandwich_souce_button.get_attribute('class') == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"


    def test_click_on_sandwich_filling_button(self, driver):
       driver.get(f'{URL}')

       driver.find_element(*StellarBurgersLocators.ENTER_BUTTON_MAIN_PAGE).click()

       driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_MAIN_PAGE).send_keys("MikhailShemakhanskiy8111@yandex.ru")

       driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_MAIN_PAGE).send_keys("1234567")

       driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()

       WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

       sandwich_filling_button = driver.find_element(*StellarBurgersLocators.SANDWICH_FILLING_BUTTON)
       sandwich_filling_button.click()
       WebDriverWait(driver, 10)

       assert sandwich_filling_button.get_attribute('class') == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"