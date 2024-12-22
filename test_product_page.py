from pages.base_page import BasePage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import pytest
import time

# default = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
# links = [f"{default}{num}" for num in range(10)]
# links[7] = pytest.param(links[7], marks=pytest.mark.xfail)

# @pytest.mark.parametrize('link', links)
# def test_guest_can_add_product_to_basket(browser, link):
#     page = BasePage(browser, link)
#     page.open()
#     product_page = ProductPage(browser, browser.current_url)
#     product_page.add_product_to_basket()
#     product_page.solve_quiz_and_get_code()
#     time.sleep(600)
#     product_page.should_be_similar_name()
#     product_page.should_be_similar_price()


# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"
#     page = BasePage(browser, link)
#     page.open()
#     product_page = ProductPage(browser, browser.current_url, timeout=0)
#     product_page.add_product_to_basket()
#     product_page.should_not_be_success_message()


# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"
#     page = BasePage(browser, link)
#     page.open()
#     product_page = ProductPage(browser, browser.current_url, timeout=0)
#     product_page.should_not_be_success_message()

# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2'
#     page = BasePage(browser, link)
#     page.open()
#     product_page = ProductPage(browser, browser.current_url, timeout=0)
#     product_page.add_product_to_basket()
#     product_page.should_not_be_success_message()
    
# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
    
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()
    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    basket_page = BasketPage(browser, browser.current_url, timeout=0)
    basket_page.go_to_basket_page()
    basket_page.should_not_be_basket_items()
    basket_page.should_be_text_basket_empty()