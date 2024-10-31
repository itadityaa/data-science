from dotenv import load_dotenv
import os

load_dotenv()
KAGGLE_USERNAME = os.getenv('KAGGLE_USERNAME')
KAGGLE_KEY = os.getenv('KAGGLE_KEY')
DATASET_URL = os.getenv('DATASET_URL')
DATASET_PATH = os.getenv('DATASET_PATH')

print(os.getcwd())
os.chdir(os.getenv('REPO_PATH'))

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

api.dataset_download_files(DATASET_URL, path=DATASET_PATH, unzip=True)