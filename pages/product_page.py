from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_product = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_product.click()
        self.solve_quiz_and_get_code()

        #self.should_be_message_contain_book_name()
        #self.should_be_message_contain_the_same_price()

    def should_be_message_contain_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        message = self.browser.find_element(*ProductPageLocators.ALERT_MESSAGE).text
        #print(book_name, message)
        assert book_name == message, "This book doesn't added in the basket"

    def should_be_message_contain_the_same_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        price_message = self.browser.find_element(*ProductPageLocators.ALERT_BOOK_PRICE).text
        #print(book_price, price_message)
        assert book_price == price_message, "Price doesn't match"

    def should_be_book(self):
        book_name = self.is_element_present(*ProductPageLocators.BOOK_NAME)
        assert book_name, "No name book"

    def should_be_price(self):
        book_price = self.is_element_present(*ProductPageLocators.BOOK_PRICE)
        assert book_price, "No price"

    def should_be_book_added(self):
        book_name = self.is_element_present(*ProductPageLocators.ADDED_BOOK_NAME)
        assert book_name, "No name added book"

    def should_be_price_added(self):
        book_price = self.is_element_present(*ProductPageLocators.ADDED_BOOK_PRICE)
        assert book_price, "No added price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_MESSAGE), "Success message is presented, but should not be"

    def should_not_stay_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_MESSAGE), \
            "Success message is not disappeared, but must be"




