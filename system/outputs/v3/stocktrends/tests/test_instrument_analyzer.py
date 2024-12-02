import pytest
import pandas as pd
from src.instrument_analyzer import InstrumentAnalyzer

@pytest.fixture
def analyzer():
    return InstrumentAnalyzer()

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'date': ['2021/01/01'],
        'open': [100],
        'high': [110],
        'low': [90],
        'close': [105]
    })


def test_analyze_instrument(analyzer, sample_data):
    results = analyzer.analyze_instrument(sample_data, instrument_type='stock')
    assert isinstance(results, dict)