import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data import (
    VALID_USERNAME, 
    VALID_PASSWORD, 
    INVALID_USERNAME, 
    INVALID_PASSWORD,
    ERROR_USERNAME_REQUIRED,
    ERROR_CREDENTIALS_INVALID
)

class TestLogin:
    """Test cases for login functionality"""
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Navigate to login page before each test"""
        self.login_page = LoginPage(page)
        self.inventory_page = InventoryPage(page)
        self.login_page.navigate()
    
    def test_successful_login(self, page: Page):
        """Test login with valid credentials"""
        self.login_page.login(VALID_USERNAME, VALID_PASSWORD)
        
        self.login_page.expect_login_successful()
        assert self.inventory_page.get_page_title() == "Products"
    
    def test_login_with_invalid_credentials(self, page: Page):
        """Test login with invalid credentials"""
        self.login_page.login(INVALID_USERNAME, INVALID_PASSWORD)
        
        assert self.login_page.is_error_displayed()
        self.login_page.expect_error_message(ERROR_CREDENTIALS_INVALID)
    
    def test_login_with_empty_username(self, page: Page):
        """Test login with empty username"""
        self.login_page.enter_password(VALID_PASSWORD)
        self.login_page.click_login()
        
        assert self.login_page.is_error_displayed()
        self.login_page.expect_error_message(ERROR_USERNAME_REQUIRED)
    
    def test_login_with_empty_password(self, page: Page):
        """Test login with empty password"""
        self.login_page.enter_username(VALID_USERNAME)
        self.login_page.click_login()
        
        assert self.login_page.is_error_displayed()
    
    def test_login_with_empty_fields(self, page: Page):
        """Test login with both fields empty"""
        self.login_page.click_login()
        
        assert self.login_page.is_error_displayed()
        self.login_page.expect_error_message(ERROR_USERNAME_REQUIRED)
    
    def test_logout(self, page: Page):
        """Test logout functionality"""
        self.login_page.login(VALID_USERNAME, VALID_PASSWORD)
        self.inventory_page.logout()
        
        self.login_page.expect_url(self.login_page.base_url + "/")
        assert self.login_page.is_visible(self.login_page.LOGIN_BUTTON)