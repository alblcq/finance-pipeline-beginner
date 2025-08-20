import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.types import VARCHAR, DECIMAL, INTEGER, Date
from dotenv import load_dotenv
import os
import logging

load_dotenv(dotenv_path='config/.env')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_database():
    """Sets up the database table."""
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'), 
            database=os.getenv('DB_NAME'), 
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS transactions")
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS transactions (
                            id SERIAL PRIMARY KEY,
                            transaction_date DATE,
                            amount DECIMAL(10, 2),
                            category VARCHAR(20),
                            year INTEGER,
                            month VARCHAR(10)
                       )
                    """)
        conn.commit()
        cursor.close()
        logging.info("Database table setup complete")
    except Exception as e:
        logging.error(f"Database setup failed: {str(e)}")
        raise

def load(df):
    """Loads DataFrame to Postgres DB"""
    try:
        engine_url = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
        engine = create_engine(engine_url)
        df.to_sql('transactions', con=engine, if_exists='append', index=False, chunksize=10000, method='multi', dtype={
            'transaction_date': Date,
            'category': VARCHAR(20),
            'amount': DECIMAL(10, 2),
            'year': INTEGER,
            'month': VARCHAR(10),
        })
        logging.info(f"Loaded {len(df)} rows to database")
    except Exception as e:
        logging.error(f"Load failed: {str(e)}")
        raise