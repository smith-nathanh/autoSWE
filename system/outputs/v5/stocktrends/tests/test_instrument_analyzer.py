import pytest
import pandas as pd
from src.instrument_analyzer import InstrumentAnalyzer

def test_analyze_instrument_stock():
    analyzer = InstrumentAnalyzer()
    data = pd.DataFrame({'close': [100, 102, 104, 106, 108]})
    result = analyzer.analyze_instrument(data, 'stock')
    assert result['average_close'] == 104
    assert result['max_close'] == 108
    assert result['min_close'] == 100


def test_analyze_instrument_commodity():
    analyzer = InstrumentAnalyzer()
    data = pd.DataFrame({'close': [200, 202, 204, 206, 208]})
    result = analyzer.analyze_instrument(data, 'commodity')
    assert result['average_close'] == 204
    assert result['max_close'] == 208
    assert result['min_close'] == 200