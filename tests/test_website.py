import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.browser_utils import init_browser
from page_objects.homepage import HomePage
from utils.logging_utils import setup_logger

# Initialize the logger
logger = setup_logger()

@pytest.fixture
def driver():
    # Log the browser initialization
    logger.info("Initializing the browser...")
    driver = init_browser()
    yield driver
    # Log after closing the browser
    logger.info("Closing the browser...")
    driver.quit()

def test_homepage_title(driver):
    """Test case to check if the page title contains 'detikcom'."""
    logger.info("Opening the homepage of Detik...")
    homepage = HomePage(driver)
    homepage.open()

    # Wait for the title to load (page load check)
    WebDriverWait(driver, 10).until(
        EC.title_contains("detikcom")  # Check if 'detikcom' is part of the title
    )
    
    actual_title = driver.title
    logger.info(f"Page title: {actual_title}")
    
    # Assert if 'detikcom' is in the title
    assert "detikcom" in actual_title.lower(), f"Expected title to contain 'detikcom', but got '{actual_title}'"
    logger.info("Homepage title contains 'detikcom' as expected.")

def test_search_functionality(driver):
    """Test case for the search functionality."""
    search_query = "technology"
    logger.info(f"Performing search with query: {search_query}")
    
    homepage = HomePage(driver)
    homepage.open()

    # Wait for the search box to be visible
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "search-input"))  # Ensure the search input element's locator is correct
    )

    # Interact with the search box
    search_box.send_keys(search_query)
    search_box.submit()
    
    # Log the search action
    logger.info(f"Search results loaded for query: {search_query}")
    
    # Wait for the search results to load
    search_results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".search-results"))
    )
    
    logger.info(f"Number of search results: {len(search_results)}")
    
    assert len(search_results) > 0, f"No search results found for query: {search_query}"
    logger.info("Search functionality test passed.")
