from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class CartPage(Page):
    empty_cart_text = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def verify_empty_cart_msg(self):
        actual_text = self.find_element(*self.empty_cart_text).text
        assert 'Your cart is empty' is in actual_text, f"Expected text 'Your cart is empty' not in {actual_text}"




