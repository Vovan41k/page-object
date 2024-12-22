from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def go_to_basket_page(self):
        basket = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        basket.click()
    
    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Basket is present'

    def should_be_text_basket_empty(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_TEXT).text == 'Your basket is empty. Continue shopping', 'Invalid text'