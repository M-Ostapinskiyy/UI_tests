from pages.base_page import BasePage


class FinishPage(BasePage):
    FINISH_BUTTON_SELECTOR = '[data-test="finish"]'
    MENU_BUTTON_SELECTOR = '#react-burger-menu-btn'
    LOGOUT_BUTTON_SELECTOR = '#logout_sidebar_link'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = '/checkout-step-two.html'

    def finish_order(self):
        self.wait_for_selector_and_click(self.FINISH_BUTTON_SELECTOR)
        self.wait_for_selector_and_click(self.MENU_BUTTON_SELECTOR)
        self.wait_for_selector_and_click(self.LOGOUT_BUTTON_SELECTOR)