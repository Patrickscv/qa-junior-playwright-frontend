from pages.test_finish import FinishPay

class TestFinish:
    def test_finish(self, page, sauce_base_url, standard_username, secret_password):
        page.goto(sauce_base_url)

        finish_test = FinishPay(page)
        
        finish_test.sauce_login(standard_username, secret_password)

        finish_test.add_itens()

        finish_test.checkout_itens()

        finish_test.finish_pay()
        
        finish_test.finish_verification()

