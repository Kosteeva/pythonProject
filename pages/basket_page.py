from .main_page import BasePage
from .locators import ProductPageLocators


class BasketPage(BasePage):
    def should_be_clear_basket(self):
        # проверяет текст что корзина пустае
        assert self.is_element_present(*ProductPageLocators.CLEAR_BASKET), "Basket doesn't clear"

    def should_not_be_book_in_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.BUTTON_CKECKOUT), "Basket contain book"
