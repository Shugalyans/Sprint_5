from config import URL
from locators import StellarBurgersLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import get_sign_up_data


class TestStellarBurgersRegistration:


    def test_correct_registration_but_user_exist(self, driver):
        driver.get(f'{URL}/register')
        username = driver.find_element(*StellarBurgersLocators.USERNAME_FIELD)
        username.send_keys("Mikhail")

        email = driver.find_element(*StellarBurgersLocators.EMAIL_FIELD)
        email.send_keys("MikhailShemakhanskiy8111@yandex.ru")

        password = driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD)
        password.send_keys("1234567")

        submit_button = driver.find_element(*StellarBurgersLocators.SUBMIT_BUTTON)
        submit_button.click()

        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.USER_EXIST))
        user_exist = driver.find_element(*StellarBurgersLocators.USER_EXIST)
        assert user_exist.is_displayed()

    def test_random_correct_registration_successful(self, driver):
        driver.get(f'{URL}/register')
        name_data, email_data, password_data = get_sign_up_data()
        username = driver.find_element(*StellarBurgersLocators.USERNAME_FIELD)
        username.send_keys(name_data)

        email = driver.find_element(*StellarBurgersLocators.EMAIL_FIELD)
        email.send_keys(email_data)

        password = driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD)
        password.send_keys(password_data)

        submit_button = driver.find_element(*StellarBurgersLocators.SUBMIT_BUTTON)
        submit_button.click()

        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.ENTER_BUTTON))
        enter_button = driver.find_element(*StellarBurgersLocators.ENTER_BUTTON)
        assert enter_button.is_displayed()


    def test_wrong_password_during_registration(self,driver):
        driver.get(f'{URL}/register')
        username = driver.find_element(*StellarBurgersLocators.USERNAME_FIELD)
        username.send_keys("Mikhail")

        email = driver.find_element(*StellarBurgersLocators.EMAIL_FIELD)
        email.send_keys("MikhailShemakhanskiy8111@yandex.ru")

        password = driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD)
        password.send_keys("12345")

        submit_button = driver.find_element(*StellarBurgersLocators.SUBMIT_BUTTON)
        submit_button.click()

        assert driver.find_element(*StellarBurgersLocators.WRONG_PASSWORD).text == 'Некорректный пароль'




