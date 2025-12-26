from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class InventoryPage(BasePage):
    """Page Object for the Inventory/Products page"""
    
    # Locators
    TITLE = ".title"
    INVENTORY_ITEMS = ".inventory_item"
    INVENTORY_ITEM_NAME = ".inventory_item_name"
    INVENTORY_ITEM_PRICE = ".inventory_item_price"
    SHOPPING_CART_LINK = ".shopping_cart_link"
    SHOPPING_CART_BADGE = ".shopping_cart_badge"
    SORT_DROPDOWN = ".product_sort_container"
    BURGER_MENU = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
    
    def get_page_title(self) -> str:
        """Get page title text"""
        return self.get_text(self.TITLE)
    
    def get_product_count(self) -> int:
        """Get number of products displayed"""
        return self.page.locator(self.INVENTORY_ITEMS).count()
    
    def add_item_to_cart(self, item_name: str):
        """Add item to cart by item name (e.g., 'sauce-labs-backpack')"""
        button_id = f"#add-to-cart-{item_name}"
        self.click(button_id)
    
    def remove_item_from_cart(self, item_name: str):
        """Remove item from cart by item name"""
        button_id = f"#remove-{item_name}"
        self.click(button_id)
    
    def get_cart_item_count(self) -> str:
        """Get the number displayed on cart badge"""
        if self.is_visible(self.SHOPPING_CART_BADGE):
            return self.get_text(self.SHOPPING_CART_BADGE)
        return "0"
    
    def click_cart(self):
        """Click shopping cart icon"""
        self.click(self.SHOPPING_CART_LINK)
    
    def sort_products(self, sort_option: str):
        """Sort products by option (az, za, lohi, hilo)"""
        self.page.select_option(self.SORT_DROPDOWN, sort_option)
    
    def get_product_names(self) -> list:
        """Get all product names"""
        return self.page.locator(self.INVENTORY_ITEM_NAME).all_text_contents()
    
    def get_product_prices(self) -> list:
        """Get all product prices as float values"""
        prices = self.page.locator(self.INVENTORY_ITEM_PRICE).all_text_contents()
        return [float(price.replace("$", "")) for price in prices]
    
    def click_product(self, item_id: str):
        """Click on a product to view details"""
        product_link = f"#item_{item_id}_title_link"
        self.click(product_link)
    
    def open_menu(self):
        """Open burger menu"""
        self.click(self.BURGER_MENU)
    
    def logout(self):
        """Logout from application"""
        self.open_menu()
        self.click(self.LOGOUT_LINK)
    
    def expect_cart_badge_count(self, count: str):
        """Assert cart badge shows expected count"""
        expect(self.page.locator(self.SHOPPING_CART_BADGE)).to_have_text(count)
    
    def expect_cart_badge_not_visible(self):
        """Assert cart badge is not visible"""
        expect(self.page.locator(self.SHOPPING_CART_BADGE)).not_to_be_visible()
    
    def expect_product_count(self, count: int):
        """Assert expected number of products"""
        expect(self.page.locator(self.INVENTORY_ITEMS)).to_have_count(count)