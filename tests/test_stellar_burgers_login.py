from config import URL
from locators import StellarBurgersLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestStellarBurgersLogin():

    def test_login_via_main_page(self, driver):
       driver.get(f'{URL}')

       submit_button = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON_MAIN_PAGE).click()

       email = driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_MAIN_PAGE).send_keys("MikhailShemakhanskiy8111@yandex.ru")

       password = driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_MAIN_PAGE).send_keys("1234567")

       submit_button = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()

       WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
       order_button = driver.find_element(*StellarBurgersLocators.ORDER_BUTTON)
       assert order_button.is_displayed()


    def test_login_via_profile_button(self, driver):
       driver.get(f'{URL}')

       submit_button = driver.find_element(*StellarBurgersLocators.PROFILE_BUTTON).click()

       email = driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_MAIN_PAGE).send_keys("MikhailShemakhanskiy8111@yandex.ru")

       password = driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_MAIN_PAGE).send_keys("1234567")

       submit_button = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()

       WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
       order_button = driver.find_element(*StellarBurgersLocators.ORDER_BUTTON)
       assert order_button.is_displayed()


    def test_login_via_register_form(self,driver):
      driver.get(f'{URL}/register')

      submit_button = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON_REGISTRATION_FORM_AND_RECOVERY_PAGE).click()

      email = driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_MAIN_PAGE).send_keys("MikhailShemakhanskiy8111@yandex.ru")

      password = driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_MAIN_PAGE).send_keys("1234567")

      submit_button = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()

      WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
      order_button = driver.find_element(*StellarBurgersLocators.ORDER_BUTTON)
      assert order_button.is_displayed()

    def test_login_via_password_recovery_form(self,driver):
      driver.get(f'{URL}/login')

      submit_button = driver.find_element(*StellarBurgersLocators.PASSWORD_RECOVERY_BUTTON).click()

      WebDriverWait(driver, 10)

      submit_button = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON_REGISTRATION_FORM_AND_RECOVERY_PAGE).click()

      email = driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_MAIN_PAGE).send_keys("MikhailShemakhanskiy8111@yandex.ru")

      password = driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_MAIN_PAGE).send_keys("1234567")

      submit_button = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()

      WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
      order_button = driver.find_element(*StellarBurgersLocators.ORDER_BUTTON)
      assert order_button.is_displayed()
