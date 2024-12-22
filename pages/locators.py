from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, 'span.btn-group > a.btn')
    BASKET_ITEMS = (By.CSS_SELECTOR, 'div.basket-items')
    BASKET_TEXT = (By.CSS_SELECTOR, 'div#content_inner p')

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, 'input[name="registration-email"]')
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, 'input[name="registration-password1"]')
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, 'input[name="registration-password2"]')
    REGISET_BUTTON_SUBMIT = (By.CSS_SELECTOR, 'button[name="registration_submit"]')

class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages div:nth-child(1)")
    PRODUCT_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    RESULT_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alertinner strong")
    RESULT_PRODUCT_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong")
