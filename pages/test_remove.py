from playwright.sync_api import expect

class RemoveItens:
    def __init__(self, page):
        self.page = page

    def sauce_login(self, standard_username, secret_password):

        expect(self.page.get_by_text("Swag Labs")).to_be_visible()
        expect(self.page.locator("[data-test=\"username\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"password\"]")).to_be_visible()

        self.page.locator("[data-test=\"username\"]").click()
        self.page.locator("[data-test=\"username\"]").fill(standard_username)
        self.page.locator("[data-test=\"password\"]").click()
        self.page.locator("[data-test=\"password\"]").fill(secret_password)
        self.page.locator("[data-test=\"login-button\"]").click()

        expect(self.page.locator("[data-test=\"title\"]")).to_be_visible()
        expect(self.page.get_by_text("Swag Labs")).to_be_visible()
        expect(self.page.locator("[data-test=\"product-sort-container\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()
    
    def add_itens(self):

        self.page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
        self.page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
        self.page.locator("[data-test=\"shopping-cart-link\"]").click()

        expect(self.page.locator("[data-test=\"cart-desc-label\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"cart-quantity-label\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"item-4-title-link\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"item-0-title-link\"]")).to_be_visible()

    def remove_and_verify_itens(self):

        self.page.locator("[data-test=\"remove-sauce-labs-bike-light\"]").click()
        
        expect(self.page.locator("[data-test=\"shopping-cart-link\"]")).to_contain_text("1")
