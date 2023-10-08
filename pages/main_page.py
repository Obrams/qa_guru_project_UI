from selene import browser, be, have


class MainPage:

    def open(self):
        browser.open('/')

    def authorization(self, login, password):
        browser.element('[data-test=username]').type(login)
        browser.element('[data-test=password]').type(password)
        browser.element('#login-button').click()
        return self

    def check_success_authorization(self):
        browser.element('[class="title"]').should(have.text('Products'))
        browser.element('.shopping_cart_container').should(be.visible)
        return self

    def logout_shop(self):
        browser.element('.bm-burger-button').click()
        browser.element('#logout_sidebar_link').click()
        return self

    def check_error_message(self, message_error):
        browser.element('[data-test=error]').should(have.text(f'Epic sadface: {message_error}'))
        browser.element('.error-button').click()
        return self

