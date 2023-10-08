import allure
from allure_commons.types import Severity

from pages.main_page import MainPage
from utils.config import Config

main_page = MainPage()

login_shop = Config.username_shop
password_shop = Config.password_shop

lock_username_shop = Config.lock_username_shop
lock_password_shop = Config.lock_password_shop

unccorected_login = Config.uncorrected_username_shop
unccorected_password = Config.uncorrected_password_shop


@allure.feature('Проверка успешной авторизации')
@allure.label('owner', 'Nikita')
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.title('Открытие страницы авторизации и проверка авторизации под корректным пользователем')
def test_authorization_success():
    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Authorization success'):
        main_page.authorization(login_shop, password_shop)

    with allure.step('Authorization success'):
        main_page.check_success_authorization()

    with allure.step('Authorization success'):
        main_page.logout_shop()


@allure.feature('Проверка авторизации с пустыми полями на форме')
@allure.label('owner', 'Nikita')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.title('Открытие страницы авторизации и проверка авторизации с незаполненной формой')
def test_authorization_with_empty_fields():
    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Authorization with empty fields'):
        main_page.authorization('', '')

    with allure.step('Check message error'):
        main_page.check_error_message('Username is required')


@allure.feature('Проверка авторизации под заблокированным пользователем')
@allure.label('owner', 'Nikita')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.title('Открытие страницы авторизации и проверка авторизации под заблокированным пользователем')
def test_authorization_lock_user():
    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Authorization lock user'):
        main_page.authorization(lock_username_shop, lock_password_shop)

    with allure.step('Check message error'):
        main_page.check_error_message('Sorry, this user has been locked out.')


@allure.feature('Проверка авторизации под не корректными данными для авторизации')
@allure.label('owner', 'Nikita')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.title('Открытие страницы авторизации и не корректными данными для авторизации')
def test_authorization_with_invalid_login_password():
    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Authorization with invalid login password'):
        main_page.authorization(unccorected_login, unccorected_password)

    with allure.step('Check message error'):
        main_page.check_error_message('Username and password do not match any user in this service')
