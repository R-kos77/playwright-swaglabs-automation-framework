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
    CHECKOUT_INFO_ALT,
    SUCCESS_ORDER_COMPLETE
)

class TestEndToEnd:
    """End-to-end test scenarios"""
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Initialize page objects"""
        self.login_page = LoginPage(page)
        self.inventory_page = InventoryPage(page)
        self.cart_page = CartPage(page)
        self.checkout_page = CheckoutPage(page)
        
        self.login_page.navigate()
    
    def test_complete_purchase_flow(self, page: Page):
        """
        Test complete purchase flow:
        1. Login
        2. Add multiple items to cart
        3. View cart
        4. Proceed to checkout
        5. Fill checkout information
        6. Complete order
        7. Return to products
        """
        # Step 1: Login
        self.login_page.login(VALID_USERNAME, VALID_PASSWORD)
        self.login_page.expect_login_successful()
        
        # Step 2: Add items to cart
        self.inventory_page.add_item_to_cart(PRODUCT_BACKPACK)
        self.inventory_page.add_item_to_cart(PRODUCT_BIKE_LIGHT)
        self.inventory_page.expect_cart_badge_count("2")
        
        # Step 3: View cart
        self.inventory_page.click_cart()
        self.cart_page.expect_on_cart_page()
        self.cart_page.expect_cart_item_count(2)
        
        # Step 4: Proceed to checkout
        self.cart_page.proceed_to_checkout()
        self.checkout_page.expect_on_step_one()
        
        # Step 5: Fill checkout information
        self.checkout_page.fill_checkout_information(
            CHECKOUT_INFO_ALT["first_name"],
            CHECKOUT_INFO_ALT["last_name"],
            CHECKOUT_INFO_ALT["postal_code"]
        )
        self.checkout_page.click_continue()
        
        # Verify overview
        self.checkout_page.expect_on_overview_page()
        assert self.checkout_page.get_overview_item_count() == 2
        self.checkout_page.expect_summary_visible()
        
        # Step 6: Complete order
        self.checkout_page.click_finish()
        self.checkout_page.expect_on_complete_page()
        assert self.checkout_page.get_completion_message() == SUCCESS_ORDER_COMPLETE
        
        # Step 7: Return to products
        self.checkout_page.click_back_to_products()
        self.inventory_page.expect_url(f"{self.inventory_page.base_url}/inventory.html")
    
    def test_purchase_single_item(self, page: Page):
        """Test purchasing a single item"""
        # Login and add one item
        self.login_page.login(VALID_USERNAME, VALID_PASSWORD)
        self.inventory_page.add_item_to_cart(PRODUCT_BACKPACK)
        
        # Complete checkout
        self.inventory_page.click_cart()
        self.cart_page.proceed_to_checkout()
        self.checkout_page.fill_checkout_information(
            CHECKOUT_INFO_ALT["first_name"],
            CHECKOUT_INFO_ALT["last_name"],
            CHECKOUT_INFO_ALT["postal_code"]
        )
        self.checkout_page.click_continue()
        self.checkout_page.click_finish()
        
        # Verify completion
        self.checkout_page.expect_order_complete()
    
    def test_modify_cart_before_checkout(self, page: Page):
        """Test modifying cart items before completing checkout"""
        # Login and add items
        self.login_page.login(VALID_USERNAME, VALID_PASSWORD)
        self.inventory_page.add_item_to_cart(PRODUCT_BACKPACK)
        self.inventory_page.add_item_to_cart(PRODUCT_BIKE_LIGHT)
        
        # Go to cart and remove one item
        self.inventory_page.click_cart()
        self.cart_page.remove_item(PRODUCT_BIKE_LIGHT)
        self.cart_page.expect_cart_item_count(1)
        
        # Complete checkout with remaining item
        self.cart_page.proceed_to_checkout()
        self.checkout_page.fill_checkout_information(
            CHECKOUT_INFO_ALT["first_name"],
            CHECKOUT_INFO_ALT["last_name"],
            CHECKOUT_INFO_ALT["postal_code"]
        )
        self.checkout_page.click_continue()
        
        # Verify only one item in overview
        assert self.checkout_page.get_overview_item_count() == 1
        
        self.checkout_page.click_finish()
        self.checkout_page.expect_order_complete()