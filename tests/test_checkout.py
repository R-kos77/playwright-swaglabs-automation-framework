import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.test_data import (
    VALID_USERNAME, 
    VALID_PASSWORD,
    PRODUCT_BACKPACK,
    PRODUCT_BIKE_LIGHT,
    CHECKOUT_INFO,
    ERROR_FIRSTNAME_REQUIRED,
    ERROR_LASTNAME_REQUIRED,
    ERROR_POSTALCODE_REQUIRED,
    SUCCESS_ORDER_COMPLETE
)

class TestCheckout:
    """Test cases for checkout process"""
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Setup: Login, add item, and navigate to cart"""
        self.login_page = LoginPage(page)
        self.inventory_page = InventoryPage(page)
        self.cart_page = CartPage(page)
        self.checkout_page = CheckoutPage(page)
        
        self.login_page.navigate()
        self.login_page.login(VALID_USERNAME, VALID_PASSWORD)
        self.login_page.wait_for_url(f"{self.login_page.base_url}/inventory.html")
        self.inventory_page.add_item_to_cart(PRODUCT_BACKPACK)
        self.inventory_page.click_cart()
    
    def test_navigate_to_checkout_step_one(self, page: Page):
        """Test clicking checkout navigates to step one"""
        self.cart_page.proceed_to_checkout()
        
        self.checkout_page.expect_on_step_one()
    
    def test_fill_checkout_information_successfully(self, page: Page):
        """Test filling checkout information and proceeding"""
        self.cart_page.proceed_to_checkout()
        
        self.checkout_page.fill_checkout_information(
            CHECKOUT_INFO["first_name"],
            CHECKOUT_INFO["last_name"],
            CHECKOUT_INFO["postal_code"]
        )
        self.checkout_page.click_continue()
        
        self.checkout_page.expect_on_overview_page()
    
    def test_checkout_with_empty_first_name(self, page: Page):
        """Test validation when first name is empty"""
        self.cart_page.proceed_to_checkout()
        
        self.checkout_page.enter_last_name(CHECKOUT_INFO["last_name"])
        self.checkout_page.enter_postal_code(CHECKOUT_INFO["postal_code"])
        self.checkout_page.click_continue()
        
        self.checkout_page.expect_error_message(ERROR_FIRSTNAME_REQUIRED)
    
    def test_checkout_with_empty_last_name(self, page: Page):
        """Test validation when last name is empty"""
        self.cart_page.proceed_to_checkout()
        
        self.checkout_page.enter_first_name(CHECKOUT_INFO["first_name"])
        self.checkout_page.enter_postal_code(CHECKOUT_INFO["postal_code"])
        self.checkout_page.click_continue()
        
        self.checkout_page.expect_error_message(ERROR_LASTNAME_REQUIRED)
    
    def test_checkout_with_empty_postal_code(self, page: Page):
        """Test validation when postal code is empty"""
        self.cart_page.proceed_to_checkout()
        
        self.checkout_page.enter_first_name(CHECKOUT_INFO["first_name"])
        self.checkout_page.enter_last_name(CHECKOUT_INFO["last_name"])
        self.checkout_page.click_continue()
        
        self.checkout_page.expect_error_message(ERROR_POSTALCODE_REQUIRED)
    
    def test_checkout_with_all_empty_fields(self, page: Page):
        """Test validation when all fields are empty"""
        self.cart_page.proceed_to_checkout()
        self.checkout_page.click_continue()
        
        self.checkout_page.expect_error_message(ERROR_FIRSTNAME_REQUIRED)
    
    def test_checkout_overview_displays_items(self, page: Page):
        """Test that checkout overview displays correct items"""
        self.cart_page.proceed_to_checkout()
        self.checkout_page.fill_checkout_information(
            CHECKOUT_INFO["first_name"],
            CHECKOUT_INFO["last_name"],
            CHECKOUT_INFO["postal_code"]
        )
        self.checkout_page.click_continue()
        
        assert self.checkout_page.get_overview_item_count() == 1
        self.checkout_page.expect_summary_visible()
    
    def test_checkout_overview_multiple_items(self, page: Page):
        """Test checkout overview with multiple items"""
        # Go back and add another item
        self.cart_page.continue_shopping()
        self.inventory_page.add_item_to_cart(PRODUCT_BIKE_LIGHT)
        self.inventory_page.click_cart()
        
        self.cart_page.proceed_to_checkout()
        self.checkout_page.fill_checkout_information(
            CHECKOUT_INFO["first_name"],
            CHECKOUT_INFO["last_name"],
            CHECKOUT_INFO["postal_code"]
        )
        self.checkout_page.click_continue()
        
        assert self.checkout_page.get_overview_item_count() == 2
    
    def test_complete_order(self, page: Page):
        """Test completing an order"""
        self.cart_page.proceed_to_checkout()
        self.checkout_page.fill_checkout_information(
            CHECKOUT_INFO["first_name"],
            CHECKOUT_INFO["last_name"],
            CHECKOUT_INFO["postal_code"]
        )
        self.checkout_page.click_continue()
        self.checkout_page.click_finish()
        
        self.checkout_page.expect_on_complete_page()
        assert self.checkout_page.get_completion_message() == SUCCESS_ORDER_COMPLETE
    
    def test_cancel_checkout_step_one(self, page: Page):
        """Test canceling checkout at step one returns to cart"""
        self.cart_page.proceed_to_checkout()
        self.checkout_page.click_cancel()
        
        self.cart_page.expect_on_cart_page()
    
    def test_cancel_checkout_step_two(self, page: Page):
        """Test canceling checkout at step two returns to inventory"""
        self.cart_page.proceed_to_checkout()
        self.checkout_page.fill_checkout_information(
            CHECKOUT_INFO["first_name"],
            CHECKOUT_INFO["last_name"],
            CHECKOUT_INFO["postal_code"]
        )
        self.checkout_page.click_continue()
        self.checkout_page.click_cancel()
        
        self.inventory_page.expect_url(f"{self.inventory_page.base_url}/inventory.html")
    
    def test_back_to_products_after_completion(self, page: Page):
        """Test back to products button after order completion"""
        self.cart_page.proceed_to_checkout()
        self.checkout_page.fill_checkout_information(
            CHECKOUT_INFO["first_name"],
            CHECKOUT_INFO["last_name"],
            CHECKOUT_INFO["postal_code"]
        )
        self.checkout_page.click_continue()
        self.checkout_page.click_finish()
        self.checkout_page.click_back_to_products()
        
        self.inventory_page.expect_url(f"{self.inventory_page.base_url}/inventory.html")