from config import URL
from locators import StellarBurgersLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestStellarBurgersWorkWithProfile():

    def test_click_on_user_profile_button(self, driver):
       driver.get(f'{URL}')

       driver.find_element(*StellarBurgersLocators.ENTER_BUTTON_MAIN_PAGE).click()

       driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_MAIN_PAGE).send_keys("MikhailShemakhanskiy8111@yandex.ru")

       driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_MAIN_PAGE).send_keys("1234567")

       driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()

       WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

       driver.find_element(*StellarBurgersLocators.PROFILE_BUTTON).click()

       WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.SAVE_BUTTON))
       save_button = driver.find_element(*StellarBurgersLocators.SAVE_BUTTON)
       assert save_button.is_displayed()

    def test_go_to_constructor_from_user_profile_by_click_on_StellaBurgerButton(self, driver):
       driver.get(f'{URL}')

       driver.find_element(*StellarBurgersLocators.ENTER_BUTTON_MAIN_PAGE).click()

       driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_MAIN_PAGE).send_keys("MikhailShemakhanskiy8111@yandex.ru")

       driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_MAIN_PAGE).send_keys("1234567")

       driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()

       WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

       driver.find_element(*StellarBurgersLocators.PROFILE_BUTTON).click()

       WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.SAVE_BUTTON))

       driver.find_element(*StellarBurgersLocators.STELLAR_BURGERS_BUTTON).click()
       WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
       order_button = driver.find_element(*StellarBurgersLocators.ORDER_BUTTON)
       assert order_button.is_displayed()

    def test_go_to_constructor_from_user_profile_by_click_on_ConstructorButton(self, driver):
       driver.get(f'{URL}')

       driver.find_element(*StellarBurgersLocators.ENTER_BUTTON_MAIN_PAGE).click()

       driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_MAIN_PAGE).send_keys("MikhailShemakhanskiy8111@yandex.ru")

       driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_MAIN_PAGE).send_keys("1234567")

       driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()

       WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

       driver.find_element(*StellarBurgersLocators.PROFILE_BUTTON).click()

       WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.SAVE_BUTTON))

       driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_BUTTON).click()
       WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))
       order_button = driver.find_element(*StellarBurgersLocators.ORDER_BUTTON)
       assert order_button.is_displayed()

    def test_logout(self, driver):
       driver.get(f'{URL}')

       driver.find_element(*StellarBurgersLocators.ENTER_BUTTON_MAIN_PAGE).click()

       driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_MAIN_PAGE).send_keys("MikhailShemakhanskiy8111@yandex.ru")

       driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_MAIN_PAGE).send_keys("1234567")

       driver.find_element(*StellarBurgersLocators.ENTER_BUTTON).click()

       WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ORDER_BUTTON))

       driver.find_element(*StellarBurgersLocators.PROFILE_BUTTON).click()

       WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.SAVE_BUTTON))

       driver.find_element(*StellarBurgersLocators.LOGOUT_BUTTON).click()
       WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ENTER_BUTTON))
       enter_button = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON)
       assert enter_button.is_displayed()