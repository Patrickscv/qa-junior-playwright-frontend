from pages.test_login import SauceLogin

class TestLogin:
    def test_login_sucess(self, page, sauce_base_url, standard_username, secret_password):
        page.goto(sauce_base_url)

        sauce_login = SauceLogin(page)
        
        sauce_login.sucess_login(standard_username, secret_password)
        
    def test_login_fail(self, page, sauce_base_url):
        page.goto(sauce_base_url)

        sauce_login = SauceLogin(page)

        sauce_login.fail_login()

        sauce_login.verify_fail_login()

        

        



        

