import pytest
import pandas as pd
from src.financial_data_processor import FinancialDataProcessor

def test_load_data():
    processor = FinancialDataProcessor()
    data = processor.load_data('data/unit_samples/HOOLI.csv')
    assert not data.empty


def test_preprocess_data():
    processor = FinancialDataProcessor()
    data = pd.DataFrame({'Date': ['2021-01-01'], 'Open': [100]})
    preprocessed_data = processor.preprocess_data(data)
    assert 'date' in preprocessed_data.columns
    assert 'open' in preprocessed_data.columns