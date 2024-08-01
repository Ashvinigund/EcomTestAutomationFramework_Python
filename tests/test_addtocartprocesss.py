from webdriver_manager.core import driver

from pages.Homepage import HomePage
from pages.addtocartprocess import AddToCartPage
from tests.BaseTest import BaseTest


class Testaddtocartprocess(BaseTest):

    def test_navigate_to_last_page(self):
        home_page = HomePage(self.driver)
        addtocartprocesspage = AddToCartPage(self.driver)
        addtocartprocesspage.navigate_to_last_page()

        addtocartprocesspage.do_click_last_product("MacBook Pro")
        addtocartprocesspage.add_to_cart()

        self.handle_alert(self.driver, expected_text="Product added")
        return home_page.navigate_to_homepage()
