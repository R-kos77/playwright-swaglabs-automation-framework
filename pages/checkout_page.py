from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    """Page Object for the Checkout pages (step one, step two, and complete)"""
    
    # Step One Locators
    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POSTAL_CODE_INPUT = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    CANCEL_BUTTON = "#cancel"
    ERROR_MESSAGE = "[data-test='error']"
    
    # Step Two Locators
    CART_ITEMS = ".cart_item"
    SUMMARY_INFO = ".summary_info"
    SUMMARY_TOTAL = ".summary_total_label"
    FINISH_BUTTON = "#finish"
    
    # Complete Page Locators
    COMPLETE_HEADER = ".complete-header"
    BACK_TO_PRODUCTS_BUTTON = "#back-to-products"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
    
    # Step One Methods
    def enter_first_name(self, first_name: str):
        """Enter first name"""
        self.fill(self.FIRST_NAME_INPUT, first_name)
    
    def enter_last_name(self, last_name: str):
        """Enter last name"""
        self.fill(self.LAST_NAME_INPUT, last_name)
    
    def enter_postal_code(self, postal_code: str):
        """Enter postal code"""
        self.fill(self.POSTAL_CODE_INPUT, postal_code)
    
    def fill_checkout_information(self, first_name: str, last_name: str, postal_code: str):
        """Fill all checkout information fields"""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
    
    def click_continue(self):
        """Click continue button"""
        self.click(self.CONTINUE_BUTTON)
    
    def click_cancel(self):
        """Click cancel button"""
        self.click(self.CANCEL_BUTTON)
    
    def get_error_message(self) -> str:
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def expect_error_message(self, message: str):
        """Assert error message contains expected text"""
        expect(self.page.locator(self.ERROR_MESSAGE)).to_contain_text(message)
    
    # Step Two Methods
    def get_overview_item_count(self) -> int:
        """Get number of items in checkout overview"""
        return self.page.locator(self.CART_ITEMS).count()
    
    def click_finish(self):
        """Click finish button"""
        self.click(self.FINISH_BUTTON)
    
    def expect_on_overview_page(self):
        """Assert user is on checkout overview page"""
        self.expect_url(f"{self.base_url}/checkout-step-two.html")
    
    def expect_summary_visible(self):
        """Assert summary information is visible"""
        self.expect_visible(self.SUMMARY_INFO)
    
    # Complete Page Methods
    def get_completion_message(self) -> str:
        """Get order completion message"""
        return self.get_text(self.COMPLETE_HEADER)
    
    def click_back_to_products(self):
        """Click back to products button"""
        self.click(self.BACK_TO_PRODUCTS_BUTTON)
    
    def expect_on_complete_page(self):
        """Assert user is on checkout complete page"""
        self.expect_url(f"{self.base_url}/checkout-complete.html")
    
    def expect_order_complete(self):
        """Assert order completion message is correct"""
        self.expect_text(self.COMPLETE_HEADER, "Thank you for your order!")
    
    # Common Methods
    def expect_on_step_one(self):
        """Assert user is on checkout step one"""
        self.expect_url(f"{self.base_url}/checkout-step-one.html")