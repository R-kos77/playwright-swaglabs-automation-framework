from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Page Object for the Login page"""
    
    # Locators
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page
    
    def navigate(self):
        """Navigate to login page"""
        self.navigate_to("/")
    
    def enter_username(self, username: str):
        """Enter username"""
        self.fill(self.USERNAME_INPUT, username)
    
    def enter_password(self, password: str):
        """Enter password"""
        self.fill(self.PASSWORD_INPUT, password)
    
    def click_login(self):
        """Click login button"""
        self.click(self.LOGIN_BUTTON)
    
    def login(self, username: str, password: str):
        """Perform complete login action"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
    def get_error_message(self) -> str:
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self) -> bool:
        """Check if error message is displayed"""
        return self.is_visible(self.ERROR_MESSAGE)
    
    def expect_error_message(self, message: str):
        """Assert error message contains expected text"""
        expect(self.page.locator(self.ERROR_MESSAGE)).to_contain_text(message)
    
    def expect_login_successful(self):
        """Assert that login was successful"""
        self.expect_url(f"{self.base_url}/inventory.html")