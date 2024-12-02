import pytest
import pandas as pd
from src.financial_data_processor import FinancialDataProcessor

@pytest.fixture
def processor():
    return FinancialDataProcessor()

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'Date': ['2021/01/01'],
        'Open': [100],
        'High': [110],
        'Low': [90],
        'Close': [105]
    })

def test_load_data(processor):
    data = processor.load_data('unit_samples/HOOLI.csv')
    assert not data.empty


def test_preprocess_data(processor, sample_data):
    preprocessed_data = processor.preprocess_data(sample_data)
    assert 'date' in preprocessed_data.columns