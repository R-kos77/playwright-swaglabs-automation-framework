import sys
from pathlib import Path

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).parent))

import pytest

def pytest_configure(config):
    """
    Configure pytest with custom markers
    """
    config.addinivalue_line(
        "markers", "smoke: mark test as part of smoke test suite"
    )
    config.addinivalue_line(
        "markers", "regression: mark test as part of regression test suite"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test results and take screenshots on failure
    """
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        # Get the page fixture if it exists
        page = item.funcargs.get("page")
        if page:
            # Take screenshot on failure
            screenshot_path = f"screenshots/{item.name}.png"
            try:
                page.screenshot(path=screenshot_path)
                print(f"\nScreenshot saved: {screenshot_path}")
            except:
                pass  # Ignore if screenshot fails