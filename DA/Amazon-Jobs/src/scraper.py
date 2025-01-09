from logger import get_logger
from bs4 import BeautifulSoup
import requests as req
import yaml
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Scraper:
    """
    A class for web scraping, processing, and saving data using Selenium and BeautifulSoup.

    Attributes:
        config (dict): Configuration dictionary loaded from a YAML file.
        url (str): Base URL for scraping.
        data_path (str): Path to the directory where data will be saved.
        data_file (str): Path to the file where processed data will be saved.
        driver (webdriver): Selenium WebDriver instance for interacting with the web.
    """

    def __init__(self, config_path: str, project_dir: str):
        """
        Initializes the Scraper with configuration and sets up paths.

        Args:
            config_path (str): Path to the configuration YAML file.
            project_dir (str): Path to the root of the project directory.
        """
        self.config = self.load_config(config_path)
        self.url = self.config['base_url']
        self.data_path = os.path.join(project_dir, self.config['download']['download_dir'])
        self.data_file = os.path.join(self.data_path, self.config['download']['download_file'])
        os.makedirs(self.data_path, exist_ok=True)

        # Set up Selenium WebDriver
        chrome_service = Service(self.config['selenium']['driver_path'])
        self.driver = webdriver.Chrome(service=chrome_service)

        logger.info(f"Starting to scrape data from: {self.url}")
        self.get_data()
        logger.info("Data scraping completed successfully.")

        logger.info("Processing data.")
        self.process_data()
        logger.info("Data processing completed successfully.")

        logger.info(f"Saving data to: {self.data_file}")
        self.save_data()
        logger.info("Data saved successfully.")

    def load_config(self, config_path: str) -> dict:
        """
        Loads the configuration from a YAML file.

        Args:
            config_path (str): Path to the configuration YAML file.

        Returns:
            dict: Configuration dictionary.
        """
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)

    def get_data(self):
        """
        Fetches the HTML content of the URL using Selenium and clicks the search button.
        """
        self.driver.get(self.url)
        try:
            search_button = self.driver.find_element(By.CLASS_NAME, 'btn.location-search.form-control')
            search_button.click()
            logger.info("Clicked the search button successfully.")
        except Exception as e:
            logger.error(f"Failed to click the search button: {e}")

    def process_data(self):
        """
        Processes the scraped data. Override this method for specific processing tasks.
        """
        pass

    def save_data(self):
        """
        Saves the processed data to a file. Override this method to customize saving logic.
        """
        pass

    def close(self):
        """
        Closes the Selenium WebDriver.
        """
        self.driver.quit()

if __name__ == '__main__':
    logger = get_logger(__name__)
    logger.info("Scraper script started.")

    PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(PROJECT_DIR, "config.yml")

    try:
        scraper = Scraper(config_path, PROJECT_DIR)
        logger.info("Scraper execution completed successfully.")
    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
    finally:
        scraper.close()
