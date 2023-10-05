from selene import browser, have


class Products_page:
    def add_product_for_basket(self):
        browser.all('[class^=inventory_item][class*=inventory_item_label]').element_by(have.Browser.element('#add-to-cart-sauce-labs-backpack')).click()
        return self
    #// *[ @ id = "add-to-cart-sauce-labs-backpack"]
