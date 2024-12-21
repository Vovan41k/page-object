from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_BUTTON)
        product.click()

    def should_be_similar_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        result_name = self.browser.find_element(*ProductPageLocators.RESULT_PRODUCT_NAME)
        assert product_name.text == result_name.text, 'Invalid name'

    def should_be_similar_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        result_price = self.browser.find_element(*ProductPageLocators.RESULT_PRODUCT_PRICE)
        assert product_price.text == result_price.text, 'Invalid price'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"