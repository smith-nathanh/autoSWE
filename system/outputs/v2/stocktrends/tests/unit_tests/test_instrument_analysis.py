import pytest
import pandas as pd
from src.instrument_analyzer import InstrumentAnalyzer

@pytest.fixture
def sample_data():
    return pd.read_csv('data/unit_samples/HOOLI.csv')


def test_analyze_instrument(sample_data):
    analyzer = InstrumentAnalyzer()
    analysis_results = analyzer.analyze_instrument(sample_data, instrument_type='stock')
    assert 'analysis' in analysis_results
