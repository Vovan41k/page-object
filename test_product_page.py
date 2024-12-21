from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
import pytest
import time

# default = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
# links = [f"{default}{num}" for num in range(10)]
# links[7] = pytest.param(links[7], marks=pytest.mark.xfail)

# @pytest.mark.parametrize('link', links)
# def test_guest_can_add_product(browser, link):
#     page = MainPage(browser, link)
#     page.open()
#     product_page = ProductPage(browser, browser.current_url)
#     product_page.add_product_to_basket()
#     product_page.solve_quiz_and_get_code()
#     time.sleep(600)
#     product_page.should_be_similar_name()
#     product_page.should_be_similar_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url, timeout=0)
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url, timeout=0)
    product_page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2'
    page = MainPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url, timeout=0)
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()