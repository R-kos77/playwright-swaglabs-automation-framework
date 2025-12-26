import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data import (
    VALID_USERNAME, 
    VALID_PASSWORD,
    PRODUCT_BACKPACK,
    PRODUCT_BIKE_LIGHT,
    SORT_AZ,
    SORT_ZA,
    SORT_PRICE_LOW_HIGH
)

class TestInventory:
    """Test cases for inventory/products page"""
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Login and navigate to inventory page before each test"""
        self.login_page = LoginPage(page)
        self.inventory_page = InventoryPage(page)
        
        self.login_page.navigate()
        self.login_page.login(VALID_USERNAME, VALID_PASSWORD)
        self.login_page.wait_for_url(f"{self.login_page.base_url}/inventory.html")
    
    def test_products_displayed(self, page: Page):
        """Test that 6 products are displayed"""
        self.inventory_page.expect_product_count(6)
    
    def test_add_single_item_to_cart(self, page: Page):
        """Test adding a single item to cart"""
        self.inventory_page.add_item_to_cart(PRODUCT_BACKPACK)
        
        self.inventory_page.expect_cart_badge_count("1")
    
    def test_add_multiple_items_to_cart(self, page: Page):
        """Test adding multiple items to cart"""
        self.inventory_page.add_item_to_cart(PRODUCT_BACKPACK)
        self.inventory_page.add_item_to_cart(PRODUCT_BIKE_LIGHT)
        
        self.inventory_page.expect_cart_badge_count("2")
    
    def test_remove_item_from_cart(self, page: Page):
        """Test removing an item from cart"""
        self.inventory_page.add_item_to_cart(PRODUCT_BACKPACK)
        self.inventory_page.remove_item_from_cart(PRODUCT_BACKPACK)
        
        self.inventory_page.expect_cart_badge_not_visible()
    
    def test_sort_products_az(self, page: Page):
        """Test sorting products A to Z"""
        self.inventory_page.sort_products(SORT_AZ)
        
        product_names = self.inventory_page.get_product_names()
        assert product_names == sorted(product_names), "Products are not sorted A-Z"
    
    def test_sort_products_za(self, page: Page):
        """Test sorting products Z to A"""
        self.inventory_page.sort_products(SORT_ZA)
        
        product_names = self.inventory_page.get_product_names()
        assert product_names == sorted(product_names, reverse=True), "Products are not sorted Z-A"
    
    def test_sort_products_price_low_to_high(self, page: Page):
        """Test sorting products by price (low to high)"""
        self.inventory_page.sort_products(SORT_PRICE_LOW_HIGH)
        
        prices = self.inventory_page.get_product_prices()
        assert prices == sorted(prices), "Products are not sorted by price (low to high)"
    
    def test_navigate_to_product_details(self, page: Page):
        """Test navigating to product details page"""
        self.inventory_page.click_product("4")
        
        self.inventory_page.expect_url(f"{self.inventory_page.base_url}/inventory-item.html?id=4")
        assert self.inventory_page.is_visible(".inventory_details_name")
    
    def test_cart_navigation(self, page: Page):
        """Test clicking cart icon navigates to cart page"""
        self.inventory_page.click_cart()
        
        self.inventory_page.expect_url(f"{self.inventory_page.base_url}/cart.html")