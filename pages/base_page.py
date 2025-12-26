from playwright.sync_api import Page, expect

class BasePage:
    """Base page class that all page objects inherit from"""
    
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://www.saucedemo.com"
    
    def navigate_to(self, path: str = ""):
        """Navigate to a specific path"""
        url = f"{self.base_url}{path}"
        self.page.goto(url)
    
    def get_current_url(self) -> str:
        """Get the current page URL"""
        return self.page.url
    
    def wait_for_url(self, url: str, timeout: int = 5000):
        """Wait for URL to match"""
        self.page.wait_for_url(url, timeout=timeout)
    
    def click(self, selector: str):
        """Click an element"""
        self.page.click(selector)
    
    def fill(self, selector: str, text: str):
        """Fill an input field"""
        self.page.fill(selector, text)
    
    def get_text(self, selector: str) -> str:
        """Get text content of an element"""
        return self.page.locator(selector).text_content()
    
    def is_visible(self, selector: str) -> bool:
        """Check if element is visible"""
        return self.page.locator(selector).is_visible()
    
    def expect_url(self, url: str):
        """Assert that current URL matches expected URL"""
        expect(self.page).to_have_url(url)
    
    def expect_visible(self, selector: str):
        """Assert that element is visible"""
        expect(self.page.locator(selector)).to_be_visible()
    
    def expect_text(self, selector: str, text: str):
        """Assert that element contains expected text"""
        expect(self.page.locator(selector)).to_have_text(text)