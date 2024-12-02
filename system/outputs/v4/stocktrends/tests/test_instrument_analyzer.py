import pytest
import pandas as pd
from src.instrument_analyzer import InstrumentAnalyzer

@pytest.fixture
def analyzer():
    return InstrumentAnalyzer()

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'close': [100, 102, 104, 106, 108, 110]
    })

def test_analyze_instrument_stock(analyzer, sample_data):
    result = analyzer.analyze_instrument(sample_data, 'stock')
    assert 'average_close' in result

def test_analyze_instrument_commodity(analyzer, sample_data):
    result = analyzer.analyze_instrument(sample_data, 'commodity')
    assert 'average_close' in result