from selenium.webdriver.common.by import By


class Locators:
    # Главная страница - Конструктор https://stellarburgers.nomoreparties.site/
    ENTER_IN_ACC_BTN = By.XPATH, './/button[text()="Войти в аккаунт"]'  # Кнопка "Войти в аккаунт"
    ORDER_BTN = By.XPATH, './/button[text()="Оформить заказ"]'  # Кнопка "Оформить заказ"
    ACC_BTN = By.XPATH, './/p[text()="Личный Кабинет"]'  # Кнопка "Личный Кабинет"
    LOGO_BTN = By.XPATH, './/div/header/nav/div/a'  # Логотип "Stellar Burgers"
    CONSTRUCTOR_BTN = By.XPATH, './/p[text()="Конструктор"]'  # Кнопка "Конструктор"
    HEADER_MK_BURGER = By.XPATH, './/h1[text()="Соберите бургер"]'  # Заголовок "Соберите бургер"
    BUNS_BTN = By.XPATH, './/span[(text()="Булки")]'  # Кнопка "Булки"
    SAUCES_BTN = By.XPATH, './/span[(text()="Соусы")]'  # Кнопка "Соусы"
    FILLINGS_BTN = By.XPATH, '//span[(text()="Начинки")]'  # Кнопка "Начинки"
    BUNS_SECTION = By.XPATH, './/h2[(text()="Булки")]'  # Список "Булки"
    SAUCES_SECTION = By.XPATH, './/h2[(text()="Соусы")]'  # Список "Соусы"
    FILLINGS_SECTION = By.XPATH, '//h2[(text()="Начинки")]'  # Список "Начинки"
    # Страница входа в Личный Кабинет https://stellarburgers.nomoreparties.site/login
    EMAIL_INPUT = By.XPATH, '//label[text()="Email"]/following-sibling::input[1]'  # Поле ввода email
    PWD_INPUT = By.XPATH, '//label[text()="Пароль"]/following-sibling::input[1]'  # Поле ввода пароля
    ENTER_BTN = By.XPATH, './/button[text()="Войти"]'  # Кнопка "Войти"
    REGISTRATION_LINK = By.XPATH, './/a[text()="Зарегистрироваться"]'  # Ссылка "Зарегистрироваться"
    RECOVER_PWD_LINK = By.XPATH, './/a[text()="Восстановить пароль"]'  # Ссылка "Восстановить пароль"
    # Страница Регистрации https://stellarburgers.nomoreparties.site/register
    REG_NAME_INPUT = By.XPATH, '//label[text()="Имя"]/following-sibling::input[1]'  # Поле ввода имени
    REG_EMAIL_INPUT = By.XPATH, '//label[text()="Email"]/following-sibling::input[1]'  # Поле ввода email
    REG_PWD_INPUT = By.XPATH, '//label[text()="Пароль"]/following-sibling::input[1]'  # Поле ввода пароля
    REG_BTN = By.XPATH, './/button[text()="Зарегистрироваться"]'  # Кнопка "Зарегистрироваться"
    ENTER_LINK = By.XPATH, './/a[text()="Войти"]'  # Ссылка "Войти"
    INCORRECT_PWD_MSG = By.XPATH, './/p[text()="Некорректный пароль"]'  # Сообщение"Некорректный пароль"
    USER_EXIST = By.XPATH, './/p[text()="Такой пользователь уже существует"]'   # Сообщение"пользователь уже существует"
    # Страница восстановления пароля https://stellarburgers.nomoreparties.site/forgot-password
    REC_EMAIL_INPUT = By.XPATH, '//label[text()="Email"]/following-sibling::input[1]'   # Поле ввода email
    RECOVER_BTN = By.XPATH, './/button[text()="Восстановить"]'   # Кнопка "Восстановить"
    # Страница профиля https://stellarburgers.nomoreparties.site/account/profile
    EXIT_BTN = By.XPATH, './/button[text()="Выход"]'   # Кнопка "Выход"
