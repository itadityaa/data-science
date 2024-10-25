import os
from pathlib import Path
import logging
# from tqdm import tqdm

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'nlp-text-summary-generator'

files_list = [
    'NLP/Text-summarization/.github/workflows/.gitkeep',
    f'NLP/Text-summarization/src/__init__.py',
    f'NLP/Text-summarization/src/components/__init__.py',
    f'NLP/Text-summarization/src/utils/__init__.py',
    f'NLP/Text-summarization/src/utils/common.py',
    f'NLP/Text-summarization/src/logging/__init__.py',
    f'NLP/Text-summarization/src/config/__init__.py',
    f'NLP/Text-summarization/src/config/configuration.py',
    f'NLP/Text-summarization/src/pipeline/__init__.py',
    f'NLP/Text-summarization/src/entity/__init__.py',
    f'NLP/Text-summarization/src/constants/__init__.py',
    'NLP/Text-summarization/config/config.yaml',
    'NLP/Text-summarization/params.yaml',
    'NLP/Text-summarization/app.py',
    'NLP/Text-summarization/main.py',
    'NLP/Text-summarization/Dockerfile',
    'NLP/Text-summarization/requirements.txt',
    'NLP/Text-summarization/setup.py',
    'NLP/Text-summarization/research/trials.ipynb'
]

for filepath in files_list: 
    file_path = Path(filepath)
    filedir, filename = os.path.split(file_path)
    
    # Create directory if it doesn't exist
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Created directory: {filedir}')
    
    # Create an empty file if it doesn't exist
    if not file_path.exists():
        file_path.touch()
        logging.info(f'Created file: {file_path}')
    else:
        logging.info(f'File already exists: {file_path}')
