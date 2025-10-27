from pages.test_remove import RemoveItens

class TestRemove:
    def test_remove_cart(self, page, sauce_base_url, standard_username, secret_password):
        page.goto(sauce_base_url)

        remove_test = RemoveItens(page)

        remove_test.sauce_login(standard_username, secret_password)

        remove_test.add_itens()

        remove_test.remove_and_verify_itens()
