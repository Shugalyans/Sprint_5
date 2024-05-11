from config import URL
from locators import StellarBurgersLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class TestStellarBurgersConstructorPage():

    def test_click_on_sandwich_button(self, driver):
       driver.get(f'{URL}')

       submit_button = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON_MAIN_PAGE).click()

       email = driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_MAIN_PAGE).send_keys("MikhailShemakhanskiy8111@yandex.ru")

       password = driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_MAIN_PAGE).send_keys("1234567")

       submit_button = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()

       WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

       sandwich_souce_button = driver.find_element(*StellarBurgersLocators.SANDWICH_SAUCE_BUTTON).click()
       WebDriverWait(driver, 10)
       sandwich_button = driver.find_element(*StellarBurgersLocators.SANDWICH_BUTTON).click()
       WebDriverWait(driver, 10)

       assert driver.find_element(By.XPATH, ".//ul[1]/a[2]/p").text == 'Краторная булка N-200i'


    def test_click_on_souce_button(self, driver):
       driver.get(f'{URL}')

       submit_button = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON_MAIN_PAGE).click()

       email = driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_MAIN_PAGE).send_keys("MikhailShemakhanskiy8111@yandex.ru")

       password = driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_MAIN_PAGE).send_keys("1234567")

       submit_button = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()

       WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

       sandwich_souce_button = driver.find_element(*StellarBurgersLocators.SANDWICH_SAUCE_BUTTON).click()
       driver.implicitly_wait(2)

       assert driver.find_element(By.XPATH, ".//ul[2]/a[1]/p").text == 'Соус Spicy-X'


    def test_click_on_sandwich_filling_button(self, driver):
       driver.get(f'{URL}')

       submit_button = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON_MAIN_PAGE).click()

       email = driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_MAIN_PAGE).send_keys("MikhailShemakhanskiy8111@yandex.ru")

       password = driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_MAIN_PAGE).send_keys("1234567")

       submit_button = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()

       WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

       sandwich_filling_button = driver.find_element(*StellarBurgersLocators.SANDWICH_FILLING_BUTTON).click()
       driver.implicitly_wait(2)

       assert driver.find_element(By.XPATH, ".//ul[3]/a[1]/p").text == 'Мясо бессмертных моллюсков Protostomia'