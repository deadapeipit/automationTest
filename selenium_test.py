import yaml
import pytest
from utils.browser_utils import init_browser
from page_objects.homepage import HomePage
from helpers.helpers import load_config

def test_dynamic_url(driver):
    config = load_config()
    homepage = HomePage(driver)
    homepage.open()
    
    # Verify the URL from the config file
    assert driver.current_url == config['base_url']
