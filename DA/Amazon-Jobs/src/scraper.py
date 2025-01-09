from logger import get_logger
from bs4 import BeautifulSoup
import requests as req
import yaml
import os

class Scraper:
    def __init__(self, config_path, project_dir):
        self.config = self.load_config(config_path)
        self.url = self.config['base_url']
        print(self.url)
        self.data_path = os.path.join(project_dir, self.config['download']['download_dir'])
        self.data_file = os.path.join(self.data_path, self.config['download']['download_file'])
        self.data = self.get_data()
        self.process_data()
        self.save_data(self.data_file)
    
    def load_config(self, config_path):
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    
    def get_data(self):
        response = req.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup)
        return soup
    
    def process_data(self):
        pass
    
    def save_data(self, data_file):
        pass

if __name__ == '__main__':
    logger = get_logger(__name__)
    PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(PROJECT_DIR, "config.yml")
    logger.info('Scraper started')
    scraper = Scraper(config_path, PROJECT_DIR)
    logger.info('Scraper object created successfully')