from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import time

# def test_guest_can_go_to_login_page(browser):
#     link = "https://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()


# def test_guest_should_see_login_link(browser):
#     link = "https://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "https://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    basket_page = BasketPage(browser, browser.current_url, timeout=0)
    basket_page.go_to_basket_page()
    basket_page.should_not_be_basket_items()
    basket_page.should_be_text_basket_empty()