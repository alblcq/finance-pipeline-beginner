import kagglehub #This library it is from Kaggle.com a website that has different types of datasets to work with.
import os #interacting with the opertating system (file systems)
import pandas as pd #dataframes
from dotenv import load_dotenv #loading .env file
import logging # logs

load_dotenv(dotenv_path='config/.env')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def download_and_extract() -> pd.DataFrame:
    """Downloads the dataset and extracts it as a DataFrame"""
    try:
        dataset = os.getenv('KAGGLE_DATASET')
        if not dataset:
            raise ValueError("KAGGLE_DATASET not set in .env")
        dataset_path = kagglehub.dataset_download(dataset)
        file_path = os.path.join(dataset_path, 'credit_card_transactions.csv')
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"CSV not found at {file_path}")
        df = pd.read_csv(file_path, header=0, encoding='utf-8')
        logging.info(f"Extracted {len(df)} rows from {file_path}")
        return df
    except Exception as e:
        logging.error(f"Extraction failed: {str(e)}")
        raise