from config import URL
from locators import StellarBurgersLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import get_sign_up_data


class TestStellarBurgersRegistration:


    def test_correct_registration_but_user_exist(self, driver):
        driver.get(f'{URL}/register')

        driver.find_element(*StellarBurgersLocators.USERNAME_FIELD).send_keys("Mikhail")

        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys("MikhailShemakhanskiy8111@yandex.ru")

        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys("1234567")

        driver.find_element(*StellarBurgersLocators.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.USER_EXIST))
        assert driver.find_element(*StellarBurgersLocators.USER_EXIST).text == 'Такой пользователь уже существует'

    def test_random_correct_registration_successful(self, driver):
        driver.get(f'{URL}/register')
        name_data, email_data, password_data = get_sign_up_data()
        driver.find_element(*StellarBurgersLocators.USERNAME_FIELD).send_keys(name_data)

        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys(email_data)

        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys(password_data)

        driver.find_element(*StellarBurgersLocators.SUBMIT_BUTTON).click()

        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ENTER_BUTTON))
        enter_button = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON)
        assert enter_button.is_displayed()


    def test_wrong_password_during_registration(self, driver):
        driver.get(f'{URL}/register')
        driver.find_element(*StellarBurgersLocators.USERNAME_FIELD).send_keys("Mikhail")

        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD).send_keys("MikhailShemakhanskiy8111@yandex.ru")

        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD).send_keys("12345")

        driver.find_element(*StellarBurgersLocators.SUBMIT_BUTTON).click()

        assert driver.find_element(*StellarBurgersLocators.WRONG_PASSWORD).text == 'Некорректный пароль'




