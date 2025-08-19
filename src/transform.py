import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Transforms the DataFrame by dropping columns, renames, standardizes, adds date components"""
    try:
        #Dropping unnecesary columns
        columns_to_drop = ['Unnamed: 0', 'merch_zipcode', 'zip', 'state', 'city', 'merchant', 'cc_num', 'first', 'last', 'gender', 'street', 'lat', 'long', 'city_pop', 'job', 'dob', 'trans_num', 'unix_time', 'merch_lat', 'merch_long', 'is_fraud', 'travel']
        df = df.drop(columns=columns_to_drop, errors='ignore')

        #renaming columns
        df = df.rename(columns={'amt': 'amount', 'trans_date_trans_time': 'transaction_date'}) #Renaming the first colum from unnamed:0 to something meaningful

        #Standardize categories
        df['category'] = df['category'].str.lower()
        category_mapping = {
            'food_dining': 'Dining',
            'grocery_pos': 'Groceries',
            'grocery_net': 'Groceries',
            'gas_transport': 'Transportation',
            'home': 'Home',
            'kids_pets': 'Kids & Pets',
            'entertainment': 'Entertainment',
            'personal_care': 'Personal Care',
            'health_fitness': 'Health & Fitness',
            'misc_pos': 'Miscellaneous',
            'misc_net': 'Miscellaneous',
            'travel': 'Travel',
            'shopping_net': 'Shopping',
            'shopping_pos': 'Shopping'
        }
        df['category'] = df['category'].replace(category_mapping)

        #Date Transformations
        #Creating different columns with the Year, Month and Date for better queries
        df['transaction_date'] = pd.to_datetime(df['transaction_date'])
        df['year'] = df['transaction_date'].dt.year
        df['month'] = df['transaction_date'].dt.month_name()
        df['transaction_date'] = df['transaction_date'].dt.date

        #handling missing values
        df['amount'] = df['amount'].fillna(0)
        df['category'] = df['category'].fillna('Unknown')

        logging.info(f"Transformed {len(df)} rows")
        return df
    except Exception as e:
        logging.error(f"Transformation failed {str(e)}")
        raise