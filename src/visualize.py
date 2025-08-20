import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os
import logging

load_dotenv(dotenv_path='config/.env')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def visualize():
    """Queries database and creates visualization graphs"""
    try:
        engine_url = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
        engine = create_engine(engine_url)
        query = "SELECT category, SUM(amount) AS Total_spent FROM transactions GROUP BY CATEGORY"
        df = pd.read_sql(query, engine)
        logging.info("Query results:\n" + df.to_string())

        plt.bar(df['category'], df['total_spent'])
        plt.xlabel('Category')
        plt.ylabel('Total Spent ($)')
        plt.title('Spending by Category')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('docs/spending_by_category.png')
        plt.show()
        logging.info("Visualization saved to docs/spending_by_category.png")
    except Exception as e:
        logging.error(f"Visualization failed: {str(e)}")
        raise