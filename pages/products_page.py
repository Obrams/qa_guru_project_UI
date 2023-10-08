from selene import browser, have, be


class Products_page:
    def add_product_for_basket(self):
        browser.element('#add-to-cart-sauce-labs-backpack').click()
        browser.element('.shopping_cart_badge').should(be.visible)
        return self

    def open_backet(self):
        browser.element('.shopping_cart_link').click()
        return self

    def check_success_add_product(self, name, price):
        browser.element('.inventory_item_name').should(have.exact_text(name))
        browser.element('.inventory_item_price').should(have.exact_text(f'${price}'))
        browser.element('.title').should(have.text('Your Cart'))
        return self


    def remove_product_for_basket(self):
        browser.element('#remove-sauce-labs-backpack').click()
        return self

    def check_after_remove_product(self):
        browser.element('.inventory_item_name').should(be.hidden)
        browser.element('.inventory_item_desc').should(be.hidden)
        browser.element('.shopping_cart_badge').should(be.hidden)
        return self

    def open_order_form(self):
        browser.element('#checkout').click()
        return self

    def input_order_form(self, firstName, lastName, postalCode):
        browser.element('[data-test="firstName"]').type(firstName)
        browser.element('[data-test="lastName"]').type(lastName)
        browser.element('[data-test="postalCode"]').type(postalCode)

        browser.element('[data-test="firstName"]').should(have.value(firstName))
        browser.element('[data-test="lastName"]').should(have.value(lastName))
        browser.element('[data-test="postalCode"]').should(have.value(postalCode))

        browser.element('#continue').click()
        return self

    def check_final_order_form(self, item_name, item_price, price_total):
        browser.element('.inventory_item_name').should(have.exact_text(item_name))
        browser.element('.inventory_item_price').should(have.exact_text(f'${item_price}'))
        browser.element('.summary_total_label').should(have.exact_text(f'Total: ${price_total}'))

        browser.element('#finish').click()
        return self

    def check_complete_form(self):
        browser.element('.complete-header').should(have.exact_text('Thank you for your order!'))
        browser.element('.complete-text').should(have.exact_text('Your order has been dispatched, and will arrive just as fast as the pony can get there!'))
        return self

    def return_back_home(self):
        browser.element('#back-to-products').click()
        return self
