import allure
from allure_commons.types import Severity

from pages.main_page import MainPage
from pages.products_page import Products_page
from utils.config import Config

login_shop = Config.username_shop
password_shop = Config.password_shop

products_page = Products_page()
main_page = MainPage()


@allure.feature('Проверка добавления продукта в корзину')
@allure.label('owner', 'Nikita')
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.title('Открытие страницы с продуктами и добавление продукта в корзину')
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
    with allure.step('Reset  App State'):
        products_page.reset_app_state()


@allure.feature('Проверка удаления продукта из корзины')
@allure.label('owner', 'Nikita')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.title('Открытие страницы с продуктами и удаление продукта из корзины')
def test_remove_product():
    with allure.step('Open main page'):
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

    with allure.step('Reset  App State'):
        products_page.reset_app_state()



@allure.feature('Проверка полного пути оформления продукта')
@allure.label('owner', 'Nikita')
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.title('Открытие страницы с продуктами и оформление продукта')
def test_product_purchase():
    with allure.step('Open main page'):
        main_page.open()

    with allure.step('Authorization success'):
        main_page.authorization(login_shop, password_shop)

    with allure.step('Add product for basket'):
        products_page.add_product_for_basket()

    with allure.step('Open basket'):
        products_page.open_backet()

    with allure.step('Open checkout form'):
        products_page.open_order_form()

    with allure.step('Open input order form'):
        products_page.input_order_form('User',
                                       'User',
                                       '000000')

    with allure.step('Check final order form'):
        products_page.check_final_order_form('Sauce Labs Backpack',
                                             '29.99',
                                             '32.39')

    with allure.step('Check complete order form'):
        products_page.check_complete_form()

    with allure.step('Return home page'):
        products_page.return_back_home()

    with allure.step('Logout from shop'):
        main_page.logout_shop()

