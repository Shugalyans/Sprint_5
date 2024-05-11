import random
from random import randint

#создали файл для генерации случайных данных для регистрации
def get_sign_up_data():
    email = f'email'+str(randint(0,1000))+'@mail.ru'
    password = f'12345678'+str(randint(0,1000))
    name = f'Михаил'+str(randint(0,1000))
    return name,email,password