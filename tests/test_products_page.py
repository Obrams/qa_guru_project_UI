import allure

from pages.main_page import MainPage
from pages.products_page import Products_page
from utils.config import Config

login_shop = Config.username_shop
password_shop = Config.password_shop

products_page = Products_page()
main_page = MainPage()


def test_add_product():
    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Authorization success'):
        main_page.authorization(login_shop, password_shop)

    with allure.step('Add product for basket'):
        products_page.add_product_for_basket()

    with allure.step('Open basket'):
        products_page.open_backet()

    with allure.step('Check basket after add product'):
        products_page.check_success_add_product('Sauce Labs Backpack',
                                                '29.99')


def test_remove_product():
    with allure.step('Authorization success'):
        main_page.open()

    with allure.step('Authorization success'):
        main_page.authorization(login_shop, password_shop)

    with allure.step('Add product for basket'):
        products_page.add_product_for_basket()

    with allure.step('Open basket'):
        products_page.open_backet()

    with allure.step('Remove product for basket'):
        products_page.remove_product_for_basket()

    with allure.step('Check basket after remove product'):
        products_page.check_after_remove_product()

