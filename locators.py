from selenium.webdriver.common.by import By

class StellarBurgersLocators:

    USERNAME_FIELD = (By.XPATH, "//label[text()='Имя']/../input")  # поле "Имя" на странице регистрации
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/../input")  # поле "E-mail" на странице регистрации
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/../input")  # поле "Пароль" на странице регистрации
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка "Зарегистрироваться" на странице регистрации
    WRONG_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']")  # информационная табличка "Некорректный пароль" на странице регистрации
    USER_EXIST = (By.XPATH, "//p[text()='Такой пользователь уже существует']")  # информационная табличка "Такой пользователь уже существует" на странице регистрации
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")  # кнопка "Войти" на странице входа в аккаунт
    ENTER_BUTTON_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт" на главной странице
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # кнопка "Оформить заказ" на главной странице после входа в аккаунт
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']") # кнопка "Личный кабинет" на главной странице
    ENTER_BUTTON_REGISTRATION_FORM_AND_RECOVERY_PAGE = (By.XPATH, "//a[text()='Войти']")  # кнопка "Войти" на странице формы регистрации и восстановления пароля
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")  # кнопка "Восстановить пароль" на странице входа в аккаунт
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")  # Кнопка "Сохранить" в личном кабинете
    STELLAR_BURGERS_BUTTON = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Кнопка-эмблема "Stellar burgers" в шапке любой страницы сайта https://stellarburgers.nomoreparties.site/
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка-эмблема "Конструктор" в шапке любой страницы сайта https://stellarburgers.nomoreparties.site/
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка "Выход" в личном кабинете
    SANDWICH_BUTTON = (By.XPATH, "//span[text()='Булки']")  # Кнопка "Булки" на странице конструктора
    SANDWICH_SAUCE_BUTTON = (By.XPATH, "//span[text()='Соусы']")  # Кнопка "Соусы" на странице конструктора
    SANDWICH_FILLING_BUTTON = (By.XPATH, "//span[text()='Начинки']")  # Кнопка "Начинки" на странице конструктора
    ACTIVE_TAB = (By.XPATH, './/div[contains(@class, "current")]/span') # Активный раздел на странице конструктора