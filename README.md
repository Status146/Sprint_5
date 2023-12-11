# qa_python_5
___
## Содержание:

### `conftest.py`  
- файл pytest, предназначенный для хранения фикстур
### `data.py`  
- файл содержащий в себе данные для хранения данные для входа в аккаунт
### `locators.py`  
- файл содержащий в себе локаторы, используемые на страницах
### `tests`  
- папка которая содержит в себе тестовые файлы
___

## Описание файлов в папке tests:

### 1. test_account.py:

1.1 `test_account_page` - переход по клику на «Личный кабинет»  
1.2 `test_constructor_conversion` - переход по клику на «Конструктор»  
1.3 `test_logo_conversion` - переход по клику на логотип Stellar Burgers  
1.4 `test_logout`- выход по кнопке «Выйти» в личном кабинете

### 2. test_constructor.py:

2.1 `test_buns_conversion_from_filling` - переход к разделу «Булки» через раздел «Начинки»  
2.2 `test_filling_conversion` - переход к разделу «Начинки»  
2.3 `test_sauces_conversion` - переход к разделу «Соусы»

### 3. test_login.py:

3.1 `test_login_from_lk` - вход через кнопку «Личный кабинет»  
3.2 `test_login_from_main_page` - вход по кнопке «Войти в аккаунт» на главной  
3.3 `test_login_from_recover` - вход через кнопку в форме восстановления пароля  
3.4 `test_login_from_registration` - вход через кнопку в форме регистрации

### 4. test_registration.py:

4.1 `test_registration_empty_email` - регистрация не завершена, поле email пустое
4.2 `test_registration_empty_name` - регистрация не завершена, поле имя пустое  
4.3 `test_registration_pwd_not_valid` - регистрация не завершена, некорректный пароль  
4.4 `test_registration_user_exist` - регистрация не завершена, пользователь существует  
4.5 `test_registration_user_succes` - успешная регистрация


### 5. test_login.py:

5.1 `login` - шаблонный вход в аккаунт  
5.2 `register` - шаблон для использования данных при регистрации пользователя
