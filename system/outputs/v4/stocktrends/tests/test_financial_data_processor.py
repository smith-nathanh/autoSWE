import pytest
import pandas as pd
from src.financial_data_processor import FinancialDataProcessor

@pytest.fixture
def processor():
    return FinancialDataProcessor()

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'Date': ['2021/01/01', '2021/01/02'],
        'Open': [100, 102],
        'High': [110, 112],
        'Low': [99, 101],
        'Close': [105, 107]
    })

def test_load_data(processor):
    data = processor.load_data('data/unit_samples/HOOLI.csv')
    assert not data.empty

def test_preprocess_data(processor, sample_data):
    processed_data = processor.preprocess_data(sample_data)
    assert all(col.islower() for col in processed_data.columns)