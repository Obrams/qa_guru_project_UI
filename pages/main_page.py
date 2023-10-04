from selene import browser, be, have

from utils import config
from utils.config import Config


class MainPage:

    def open(self):
        browser.open('/')

    def authorization_success(self):
        browser.element('[data-test=username]').type(Config.username_shop)
        browser.element('[data-test=password]').type(Config.password_shop)
        browser.element('#login-button').click()

        browser.element('.title').should(have.text('Products'))
        browser.element('.shopping_cart_container').should(be.visible)

        browser.element('#react-burger-menu-btn').click()
        browser.element('#logout_sidebar_link').click()
        return self

    def authorization_unsuccessful(self):
        browser.element('[data-test=username]').type('')
        browser.element('[data-test=password]').type('')
        browser.element('#login-button').click()

        browser.element('[data-test=error]').should(have.text('Epic sadface: Username is required'))
        browser.element('.error-button').click()
        return self

    def authorization_lock_user(self):
        browser.element('[data-test=username]').type(Config.block_username_shop)
        browser.element('[data-test=password]').type(Config.block_password_shop)
        browser.element('#login-button').click()

        browser.element('[data-test=error]').should(have.text('Epic sadface: Sorry, this user has been locked out.'))
        browser.element('.error-button').click()
        return self
