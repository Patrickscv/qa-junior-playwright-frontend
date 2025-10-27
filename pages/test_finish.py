from playwright.sync_api import expect
from faker import Faker

faker = Faker()

class FinishPay:
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
        self.page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
        self.page.locator("[data-test=\"shopping-cart-link\"]").click()

        expect(self.page.locator("[data-test=\"secondary-header\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"item-4-title-link\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"item-0-title-link\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"item-1-title-link\"]")).to_be_visible()

    def checkout_itens(self):

        self.page.locator("[data-test=\"checkout\"]").click()

        expect(self.page.locator("[data-test=\"title\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"firstName\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"lastName\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"postalCode\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"continue\"]")).to_be_visible()

        self.page.locator("[data-test=\"firstName\"]").click()
        self.page.locator("[data-test=\"firstName\"]").fill(faker.name())
        self.page.locator("[data-test=\"lastName\"]").click()
        self.page.locator("[data-test=\"lastName\"]").fill(faker.name())
        self.page.locator("[data-test=\"postalCode\"]").click()
        self.page.locator("[data-test=\"postalCode\"]").fill(faker.zipcode())
        self.page.locator("[data-test=\"continue\"]").click()

    def finish_pay(self):

        expect(self.page.locator("[data-test=\"title\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"item-4-title-link\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"item-0-title-link\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"item-1-title-link\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"payment-info-label\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"shipping-info-label\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"total-info-label\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"finish\"]")).to_be_visible()

        self.page.locator("[data-test=\"finish\"]").click()
    
    def finish_verification(self):

        expect(self.page.locator("[data-test=\"complete-header\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"complete-header\"]")).to_contain_text("Thank you for your order!")
