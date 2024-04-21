from playwright.sync_api import sync_playwright
import time

from pages.cart_page import CartPage
from pages.checout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.finish_page import FinishPage


# playwright = sync_playwright().start()
# browser = playwright.chromium.launch(headless=False, slow_mo=500)
# page = browser.new_page()
# page.goto("https://www.saucedemo.com/")
# page.type(selector="[id='user-name']", text="standard_user", delay=100)
# page.fill(selector= '#password', value="secret_sauce")
# page.click(selector='.submit-button') # [class = 'submit-button']
# page.wait_for_url('https://www.saucedemo.com/inventory.html', timeout=10000)
# page.wait_for_selector('#inventory_container')
#
# button_add_card = '[data-test="add-to-cart-sauce-labs-backpack"]'
# alt_locator_for_card = '.inventory_item a:has-text("Sauce Labs Backpack")'
# card_button = '.inventory_item_description:has-text("Sauce Labs Backpack") button:has-text("Add to cart")'
#
# page.is_visible(selector=button_add_card)
# page.is_enabled(selector=button_add_card)
# # page.click(selector=button_add_card)
# # page.click(selector=alt_locator_for_card)
# page.click(card_button)
# page.is_visible('[data-test="shopping-cart-link"]')
# page.click('[data-test="shopping-cart-link"]')
# page.wait_for_url('https://www.saucedemo.com/cart.html', timeout=10000)
# button_checkout = '#checkout'
# page.wait_for_selector(button_checkout)
# page.is_visible(button_checkout)
# page.is_enabled(button_checkout)
# page.click(button_checkout)
# page.wait_for_url('https://www.saucedemo.com/checkout-step-one.html', timeout=10000)
# page.fill(selector='#first-name', value='FirstName')
# page.fill(selector='#last-name', value='LastName')
# page.fill(selector='#postal-code', value='987654321')
# button_continue = '#continue'
# page.wait_for_selector(button_continue)
# page.is_visible(button_continue)
# page.is_enabled(button_continue)
# page.click(button_continue)
# page.wait_for_url('https://www.saucedemo.com/checkout-step-two.html', timeout=10000)
# button_finish = '#finish'
# page.wait_for_selector(button_finish)
# page.is_visible(button_finish)
# page.is_enabled(button_finish)
# page.click(button_finish)
# page.wait_for_url('https://www.saucedemo.com/checkout-complete.html', timeout=10000)
# page.is_visible('#react-burger-menu-btn')
# page.click('#react-burger-menu-btn')
# button_logout = '#logout_sidebar_link'
# page.wait_for_selector(button_logout)
# page.is_visible(button_logout)
# page.is_enabled(button_logout)
# page.click(button_logout)
# page.wait_for_url('https://www.saucedemo.com/', timeout=10000)
#
#
# time.sleep(5)
#
# browser.close()
# playwright.stop()


def test_add_items_and_checkout(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    finish_page = FinishPage(page)

    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_item_to_cart()
    inventory_page.cart_contains_counter("2")
    inventory_page.go_to_cart()
    cart_page.remove_item_from_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form("John", "Doe", "12345")
    finish_page.finish_order()
