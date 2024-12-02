import pytest
import pandas as pd
from src.financial_data_processor import FinancialDataProcessor

@pytest.fixture
def sample_data():
    return pd.read_csv('data/unit_samples/HOOLI.csv')


def test_preprocess_data(sample_data):
    processor = FinancialDataProcessor()
    preprocessed_data = processor.preprocess_data(sample_data)
    assert all(preprocessed_data.columns == ['date', 'open', 'high', 'low', 'close'])
