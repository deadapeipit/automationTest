from selenium.webdriver.common.by import By
from helpers.helpers import load_config,get_url

class HomePage:
    def __init__(self, driver):
        config = load_config()
        self.driver = driver
        self.url = get_url(config)

    def open(self):
        """Navigate to the homepage URL."""
        self.driver.get(self.url)

    def get_main_article_text(self):
        """Retrieve the headline article text."""
        return self.driver.find_element(By.CSS_SELECTOR, "article h2").text

    def perform_search(self, query):
        """Enter a search query and submit."""
        search_box = self.driver.find_element(By.ID, "search-input")
        search_box.send_keys(query)
        search_box.submit()
