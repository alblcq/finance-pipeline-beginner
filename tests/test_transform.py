import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
import pytest
from src.transform import transform

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'trans_date_trans_time': ['2020-06-21 12:14:25'],
        'amt': [100.0],
        'category': ['grocery_pos'],
        'Unnamed: 0': [1]
    })

def test_transform(sample_df):
    result = transform(sample_df)
    assert 'amount' in result.columns
    assert result['category'][0] == 'Groceries'
    assert result['month'][0] == 'June'
    assert 'Unnamed: 0' not in result.columns