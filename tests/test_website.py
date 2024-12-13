import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.browser_utils import init_browser
from page_objects.homepage import HomePage
from utils.logging_utils import setup_logger

# Initialize the logger
logger = setup_logger()

@pytest.fixture
def driver():
    """Fixture to initialize and quit the browser."""
    logger.info("Initializing the browser...")
    driver = init_browser()
    yield driver
    logger.info("Closing the browser...")
    driver.quit()

def test_homepage_title(driver):
    """Test case to check if the page title contains 'youtube'."""
    logger.info("Opening the homepage of YouTube...")
    homepage = HomePage(driver)
    homepage.open()

    # Wait for the title to load and check for 'youtube'
    WebDriverWait(driver, 20).until(
        EC.title_contains("YouTube")
    )
    
    actual_title = driver.title
    logger.info(f"Page title: {actual_title}")
    
    # Assert if 'YouTube' is in the title
    assert "youtube" in actual_title.lower(), f"Expected title to contain 'YouTube', but got '{actual_title}'"
    logger.info("Homepage title contains 'YouTube' as expected.")

@pytest.mark.parametrize("search_query", ["technology", "music", "sports"])
def test_search_functionality(driver, search_query):
    """Test case for the search functionality."""
    try:
        logger.info(f"Performing search with query: {search_query}")
        
        homepage = HomePage(driver)
        homepage.open()

        # Wait for the search box to be visible (Updated XPath for search box)
        search_box = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/form/input'))  # Updated to use input ID
        )
        
        # Ensure the search icon is clickable before interacting (Updated XPath for search icon)
        search_icon = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="center"]/yt-searchbox/button'))  # Updated to use button ID
        )
        search_icon.click()
        logger.info("Search icon clicked!")

        # Enter the search query and submit
        search_box.send_keys(search_query)
        search_box.submit()

        logger.info(f"Search results loaded for query: {search_query}")

        # Wait for the search results to be present
        results = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//ytd-video-renderer"))
        )
        assert len(results) > 0, f"No search results found for query '{search_query}'"
        
        for result in results:
            title = result.find_element(By.XPATH, ".//a[@id='video-title']")
            assert search_query.lower() in title.text.lower(), f"Article title '{title.text}' does not contain '{search_query}'"

        logger.info(f"Search functionality test passed for query '{search_query}'.")

    except TimeoutException as e:
        logger.error(f"Timeout occurred while waiting for the search box to be visible or search results to load. Error: {e}")
        driver.save_screenshot(f"timeout_error_screenshot_{search_query}.png")  # Save screenshot for debugging
        assert False, f"TimeoutException: {e}"

    except Exception as e:
        logger.error(f"An error occurred during the search test. Error: {e}")
        driver.save_screenshot(f"generic_error_screenshot_{search_query}.png")
        assert False, f"Error: {e}"
