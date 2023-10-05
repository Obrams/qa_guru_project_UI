from pages.main_page import MainPage
from pages.products_page import Products_page
from utils.config import Config

login_shop = Config.username_shop
password_shop = Config.password_shop

products_page = Products_page()
main_page = MainPage()


def test_add_product():
    main_page.open()

    main_page.authorization(login_shop, password_shop)

    from selene import browser
    from selene import have
    browser.element('#add-to-cart-sauce-labs-backpack').click()
