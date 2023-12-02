import random

name = "Egor"
email = "Egor_Stus_3_146@yandex.ru"
password = "2223322"


def generate_email():
    return f"Egor_Stus_3_{random.randint(100, 1000)}@yandex.ru"


def generate_password():
    return random.randint(100000, 1000000)
