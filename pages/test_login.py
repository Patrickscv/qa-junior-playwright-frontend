from playwright.sync_api import expect

class SauceLogin:
    def __init__(self, page):
        self.page = page

    def sucess_login(self, standard_username, secret_password):
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

    def fail_login(self):
        expect(self.page.get_by_text("Swag Labs")).to_be_visible()
        expect(self.page.locator("[data-test=\"username\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"password\"]")).to_be_visible()
        expect(self.page.locator("[data-test=\"login-button\"]")).to_be_visible()

        self.page.locator("[data-test=\"username\"]").click()
        self.page.locator("[data-test=\"username\"]").fill("error")
        self.page.locator("[data-test=\"password\"]").click()
        self.page.locator("[data-test=\"password\"]").fill("error")
        self.page.locator("[data-test=\"login-button\"]").click()
        
    def verify_fail_login(self):
        expect(self.page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Username and password do not match any user in this service")

    
    