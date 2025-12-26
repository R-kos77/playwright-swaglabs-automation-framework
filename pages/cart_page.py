from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CartPage(BasePage):
    """Page Object for the Shopping Cart page"""
    
    # Locators
    CART_ITEMS = ".cart_item"
    CART_ITEM_NAME = ".inventory_item_name"
    CONTINUE_SHOPPING_BUTTON = "#continue-shopping"
    CHECKOUT_BUTTON = "#checkout"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
    
    def get_cart_item_count(self) -> int:
        """Get number of items in cart"""
        return self.page.locator(self.CART_ITEMS).count()
    
    def get_cart_item_names(self) -> list:
        """Get all item names in cart"""
        return self.page.locator(self.CART_ITEM_NAME).all_text_contents()
    
    def remove_item(self, item_name: str):
        """Remove item from cart by name"""
        button_id = f"#remove-{item_name}"
        self.click(button_id)
    
    def continue_shopping(self):
        """Click continue shopping button"""
        self.click(self.CONTINUE_SHOPPING_BUTTON)
    
    def proceed_to_checkout(self):
        """Click checkout button"""
        self.click(self.CHECKOUT_BUTTON)
    
    def expect_cart_item_count(self, count: int):
        """Assert expected number of items in cart"""
        expect(self.page.locator(self.CART_ITEMS)).to_have_count(count)
    
    def expect_on_cart_page(self):
        """Assert user is on cart page"""
        self.expect_url(f"{self.base_url}/cart.html")