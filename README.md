# Playwright Swag Labs Test Automation Framework

A comprehensive test automation framework for Swag Labs built with **Python** and **Playwright**, demonstrating best practices in test automation using the **Page Object Model (POM)** design pattern.

## Features

* **Page Object Model (POM):** Clean separation of test logic and page interactions.
* **Comprehensive Test Coverage:** Login, inventory, cart, checkout, and end-to-end flows.
* **Reusable Components:** Base page class with common functionality.
* **Clear Test Data Management:** Centralized test data configuration.
* **Parallel Execution:** Support for running tests in parallel.
* **Detailed Reporting:** HTML and Allure report generation.
* **Cross-browser Testing:** Support for Chromium, Firefox, and WebKit.

## Project Structure

```text
playwright-tests/
├── pages/                    # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py          # Base page with common methods
│   ├── login_page.py         # Login page objects
│   ├── inventory_page.py     # Inventory/Products page objects
│   ├── cart_page.py          # Shopping cart page objects
│   └── checkout_page.py      # Checkout pages objects
├── tests/                    # Test files
│   ├── __init__.py
│   ├── test_login.py         # Login functionality tests
│   ├── test_inventory.py     # Product browsing tests
│   ├── test_cart.py          # Shopping cart tests
│   ├── test_checkout.py      # Checkout process tests
│   └── test_end_to_end.py    # Complete user journey tests
├── utils/                    # Utilities and test data
│   ├── __init__.py
│   └── test_data.py          # Test data constants
├── conftest.py               # Pytest configuration and fixtures
├── pytest.ini                # Pytest settings
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```
# Setup
Prerequisites
Python 3.8 or higher

pip (Python package manager)

Installation
Clone the repository


Bash

git clone https://github.com/R-kos77/playwright-swaglabs-automation-framework.git
cd playwright-tests
Create virtual environment (recommended)

Bash

python -m venv venv


# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
Install dependencies

Bash

pip install -r requirements.txt
Install Playwright browsers

Bash

playwright install
Running Tests
Run all tests

Bash

pytest
Run specific test file

Bash

pytest tests/test_login.py -v
Run specific test class

Bash

pytest tests/test_login.py::TestLogin -v
Run tests in parallel

Bash

pytest -n auto
Run with headed browser

Bash

pytest --headed
Run on specific browser

Bash

pytest --browser firefox
Reporting
Generate HTML report

Bash

pytest --html=reports/report.html --self-contained-html
Generate Allure report

Bash

# Run tests with allure
pytest --alluredir=allure-results

# Generate and open report
allure serve allure-results
Test Coverage
Login Tests
Successful login with valid credentials

Login with invalid credentials

Login with empty fields

Logout functionality

Inventory Tests
Product display verification

Add/remove items to/from cart

Product sorting (A-Z, Z-A, price)

Product details navigation

Checkout Tests
Checkout information validation

Order overview verification

Order completion

Design Patterns & Best Practices
Page Object Model (POM): Locators are defined as class constants and interactions are methods.

Base Page Pattern: Common functionality is abstracted into BasePage to reduce duplication.

Fixture Usage: Setup and teardown are handled via Pytest fixtures in conftest.py.

Adding New Tests
Create/Update Page Object

Python

# pages/new_page.py
from pages.base_page import BasePage

class NewPage(BasePage):
    ELEMENT_LOCATOR = "#element-id"

    def interact_with_element(self):
        self.click(self.ELEMENT_LOCATOR)
Create Test File

Python

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

GitHub: @R-kos77

Acknowledgments
Playwright Documentation

Swag Labs - Demo application for testing
