Playwright Swag Labs Test Automation Framework
A comprehensive test automation framework for Swag Labs built with Python and Playwright, demonstrating best practices in test automation using the Page Object Model (POM) design pattern.
Features
•	Page Object Model (POM): Clean separation of test logic and page interactions
•	Comprehensive Test Coverage: Login, inventory, cart, checkout, and end-to-end flows
•	Reusable Components: Base page class with common functionality
•	Clear Test Data Management: Centralized test data configuration
•	Parallel Execution: Support for running tests in parallel
•	Detailed Reporting: HTML and Allure report generation
•	Cross-browser Testing: Support for Chromium, Firefox, and WebKit
Project Structure
playwright-tests/
├── pages/                      # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py           # Base page with common methods
│   ├── login_page.py          # Login page objects
│   ├── inventory_page.py      # Inventory/Products page objects
│   ├── cart_page.py           # Shopping cart page objects
│   └── checkout_page.py       # Checkout pages objects
├── tests/                      # Test files
│   ├── __init__.py
│   ├── test_login.py          # Login functionality tests
│   ├── test_inventory.py      # Product browsing tests
│   ├── test_cart.py           # Shopping cart tests
│   ├── test_checkout.py       # Checkout process tests
│   └── test_end_to_end.py     # Complete user journey tests
├── utils/                      # Utilities and test data
│   ├── __init__.py
│   └── test_data.py           # Test data constants
├── conftest.py                 # Pytest configuration and fixtures
├── pytest.ini                  # Pytest settings
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
Setup
Prerequisites
•	Python 3.8 or higher
•	pip (Python package manager)
Installation
1.	Clone the repository
git clone <your-repo-url>
cd playwright-tests
2.	Create virtual environment (recommended)
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
3.	Install dependencies
pip install -r requirements.txt
4.	Install Playwright browsers
playwright install
Running Tests
Run all tests
pytest
Run specific test file
pytest tests/test_login.py -v
Run specific test class
pytest tests/test_login.py::TestLogin -v
Run specific test
pytest tests/test_login.py::TestLogin::test_successful_login -v
Run tests in parallel
pytest -n auto
Run with headed browser (see browser actions)
pytest --headed
Run with slow motion (for debugging)
pytest --headed --slowmo=1000
Run on specific browser
pytest --browser firefox
pytest --browser webkit
Reporting
Generate HTML report
pytest --html=reports/report.html --self-contained-html
Generate Allure report
# Run tests with allure
pytest --alluredir=allure-results

# Generate and open report
allure serve allure-results
Test Coverage
Login Tests (test_login.py)
•	Successful login with valid credentials
•	Login with invalid credentials
•	Login with empty fields
•	Logout functionality
Inventory Tests (test_inventory.py)
•	Product display verification
•	Add/remove items to/from cart
•	Product sorting (A-Z, Z-A, price)
•	Product details navigation
Cart Tests (test_cart.py)
•	View cart contents
•	Remove items from cart
•	Continue shopping functionality
•	Cart badge updates
Checkout Tests (test_checkout.py)
•	Checkout information validation
•	Order overview verification
•	Order completion
•	Cancel checkout at various stages
End-to-End Tests (test_end_to_end.py)
•	Complete purchase flow
•	Single item purchase
•	Cart modification before checkout
Design Patterns & Best Practices
Page Object Model (POM)
•	Each page is represented by a class
•	Locators are defined as class constants
•	Page interactions are methods
•	Assertions use expect() for better reliability
Base Page Pattern
•	Common functionality in BasePage
•	Reduces code duplication
•	Consistent interface across all pages
Test Data Management
•	Centralized test data in utils/test_data.py
•	Easy to maintain and update
•	Reusable across multiple tests
Fixture Usage
•	Setup and teardown in fixtures
•	Automatic page object initialization
•	Clean test methods focused on test logic
Adding New Tests
1.	Create/Update Page Object
# pages/new_page.py
from pages.base_page import BasePage

class NewPage(BasePage):
    ELEMENT_LOCATOR = "#element-id"
    
    def interact_with_element(self):
        self.click(self.ELEMENT_LOCATOR)
2.	Create Test File
# tests/test_new_feature.py
import pytest
from pages.new_page import NewPage

class TestNewFeature:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.new_page = NewPage(page)
    
    def test_new_functionality(self, page):
        self.new_page.interact_with_element()
        # Add assertions
Author
Robel Kiros
•	GitHub: @R-kos77
Acknowledgments
•	Playwright Documentation
•	Swag Labs - Demo application for testing

