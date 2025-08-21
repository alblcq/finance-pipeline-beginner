import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.extract import download_and_extract
from src.transform import transform
from src.load import setup_database, load
from src.visualize import visualize
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting ETL pipeline")
    setup_database()
    df = download_and_extract()
    df = transform(df)
    load(df)
    visualize()
    logging.info("ETL pipeline completed")

if __name__ == '__main__':
    main()