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
