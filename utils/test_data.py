"""Test data constants and configurations"""

# Valid credentials
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"

# Invalid credentials
INVALID_USERNAME = "invalid_user"
INVALID_PASSWORD = "wrong_password"

# Product names (for add to cart)
PRODUCT_BACKPACK = "sauce-labs-backpack"
PRODUCT_BIKE_LIGHT = "sauce-labs-bike-light"
PRODUCT_BOLT_TSHIRT = "sauce-labs-bolt-t-shirt"
PRODUCT_FLEECE_JACKET = "sauce-labs-fleece-jacket"
PRODUCT_ONESIE = "sauce-labs-onesie"
PRODUCT_TSHIRT_RED = "test.allthethings()-t-shirt-(red)"

# Checkout information
CHECKOUT_INFO = {
    "first_name": "John",
    "last_name": "Doe",
    "postal_code": "12345"
}

CHECKOUT_INFO_ALT = {
    "first_name": "Jane",
    "last_name": "Smith",
    "postal_code": "54321"
}

# Sort options
SORT_AZ = "az"
SORT_ZA = "za"
SORT_PRICE_LOW_HIGH = "lohi"
SORT_PRICE_HIGH_LOW = "hilo"

# Expected error messages
ERROR_USERNAME_REQUIRED = "Username is required"
ERROR_PASSWORD_REQUIRED = "Password is required"
ERROR_CREDENTIALS_INVALID = "Username and password do not match"
ERROR_FIRSTNAME_REQUIRED = "First Name is required"
ERROR_LASTNAME_REQUIRED = "Last Name is required"
ERROR_POSTALCODE_REQUIRED = "Postal Code is required"

# Expected success messages
SUCCESS_ORDER_COMPLETE = "Thank you for your order!"