from pages.base_page import BasePage


class InventoryPage(BasePage):
    ADD_TO_CART_SELECTOR_FIRST_ITEM = '[data-test="add-to-cart-sauce-labs-backpack"]'
    ADD_TO_CART_SELECTOR_SECOND_ITEM = '[data-test="add-to-cart-sauce-labs-bike-light"]'
    SHOPPING_CART_LINK_SELECTOR = '[data-test="shopping-cart-link"]'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/inventory.html'

    def add_item_to_cart(self):
        self.wait_for_selector_and_click(self.ADD_TO_CART_SELECTOR_FIRST_ITEM)
        self.wait_for_selector_and_click(self.ADD_TO_CART_SELECTOR_SECOND_ITEM)

    def cart_contains_counter(self, text):
        self.assert_text_in_element(self.SHOPPING_CART_LINK_SELECTOR, text)

    def go_to_cart(self):
        self.assert_element_is_visible(self.SHOPPING_CART_LINK_SELECTOR)
        self.wait_for_selector_and_click(self.SHOPPING_CART_LINK_SELECTOR)

