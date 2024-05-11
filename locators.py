from selenium.webdriver.common.by import By

class StellarBurgersLocators:

    USERNAME_FIELD = (By.XPATH,".//main/div/form/fieldset[1]/div/div/input") # поле "Имя" на странице регистрации
    EMAIL_FIELD = (By.XPATH,".//main/div/form/fieldset[2]/div/div/input") # поле "E-mail" на странице регистрации
    PASSWORD_FIELD = (By.XPATH,".//main/div/form/fieldset[3]/div/div/input") # поле "Пароль" на странице регистрации
    SUBMIT_BUTTON = (By.XPATH,".//main/div/form/button") # кнопка "Зарегистрироваться" на странице регистрации
    WRONG_PASSWORD = (By.XPATH,".//main/div/form/fieldset[3]/div/p") # информационная табличка "Некорректный пароль" на странице регистрации
    USER_EXIST = (By.XPATH,".//main/div/p") # информационная табличка "Такой пользователь уже существует" на странице регистрации
    ENTER_BUTTON = (By.XPATH, ".//main/div/form/button") # кнопка "Войти" на странице входа в аккаунт
    ENTER_BUTTON_MAIN_PAGE = (By.XPATH, ".//main/section[2]/div/button")  # кнопка "Войти в аккаунт" на главной странице
    EMAIL_FIELD_MAIN_PAGE = (By.XPATH,".//main/div/form/fieldset[1]/div/div/input") # поле "e-mail" на странице входа в аккаунт
    PASSWORD_FIELD_MAIN_PAGE = (By.XPATH,".//main/div/form/fieldset[2]/div/div/input") # поле "Пароль" на странице входа в аккаунт
    ORDER_BUTTON = (By.XPATH,".//main/section[2]/div/button") # кнопка "Оформить заказ" на главной странице после входа в аккаунт
    PROFILE_BUTTON = (By.XPATH,".//header/nav/a/p") # кнопка "Личный кабинет" на главной странице
    ENTER_BUTTON_REGISTRATION_FORM_AND_RECOVERY_PAGE = (By.XPATH,".//main/div/div/p/a") # кнопка "Войти" на странице формы регистрации и восстановления пароля
    PASSWORD_RECOVERY_BUTTON = (By.XPATH,".//main/div/div/p[2]/a") # кнопка "Восстановить пароль" на странице входа в аккаунт
    SAVE_BUTTON = (By.XPATH,".//main/div/div/div/div/button[2]") #Кнопка "Сохранить" в личном кабинете
    STELLAR_BURGERS_BUTTON = (By.XPATH, ".//header/nav/div/a") #Кнопка-эмблема "Stellar burgers" в шапке любой страницы сайта https://stellarburgers.nomoreparties.site/
    CONSTRUCTOR_BUTTON = (By.XPATH,".//header/nav/ul/li[1]/a") #Кнопка-эмблема "Конструктор" в шапке любой страницы сайта https://stellarburgers.nomoreparties.site/
    LOGOUT_BUTTON = (By.XPATH, ".//main/div/nav/ul/li[3]/button") #Кнопка "Выйти" в личном кабинете
    SANDWICH_BUTTON = (By.XPATH, ".//section[1]/div[1]/div[1]") #Кнопка "Булки" на странице конструктора
    SANDWICH_SAUCE_BUTTON = (By.XPATH, ".//section[1]/div[1]/div[2]") #Кнопка "Соусы" на странице конструктора
    SANDWICH_FILLING_BUTTON = (By.XPATH, ".//section[1]/div[1]/div[3]") #Кнопка "Начинки" на странице конструктора