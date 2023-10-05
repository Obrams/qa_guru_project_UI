import allure

from pages.main_page import MainPage
from utils.config import Config

main_page = MainPage()

login_shop = Config.username_shop
password_shop = Config.password_shop

lock_username_shop = Config.lock_username_shop
lock_password_shop = Config.lock_password_shop

unccorected_login = Config.uncorrected_username_shop
unccorected_password = Config.uncorrected_password_shop


def test_authorization_success():
    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Authorization success'):
        main_page.authorization(login_shop, password_shop)

    with allure.step('Authorization success'):
        main_page.check_success_authorization()

    with allure.step('Authorization success'):
        main_page.logout_shop()


def test_authorization_unsuccessful():
    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Authorization with empty fields'):
        main_page.authorization('', '')

    with allure.step('Check message error'):
        main_page.check_error_message('Username is required')


def test_authorization_lock_user():
    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Authorization lock user'):
        main_page.authorization(lock_username_shop, lock_password_shop)

    with allure.step('Check message error'):
        main_page.check_error_message('Sorry, this user has been locked out.')


def test_authorization_with_invalid_login_password():
    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Authorization with invalid login password'):
        main_page.authorization(unccorected_login, unccorected_password)

    with allure.step('Check message error'):
        main_page.check_error_message('Username and password do not match any user in this service')
