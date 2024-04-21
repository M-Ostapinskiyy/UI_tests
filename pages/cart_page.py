from pages.base_page import BasePage


class CartPage(BasePage):
    REMOVE_ITEM_SELECTOR = '[data-test="remove-sauce-labs-backpack"]'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/cart.html'

    def remove_item_from_cart(self):
        self.wait_for_selector_and_click(self.REMOVE_ITEM_SELECTOR)