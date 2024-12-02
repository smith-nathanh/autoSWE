import pytest
import pandas as pd
from src.indicator_calculator import IndicatorCalculator

@pytest.fixture
def calculator():
    return IndicatorCalculator()

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'date': ['2021/01/01'],
        'open': [100],
        'high': [110],
        'low': [90],
        'close': [105]
    })


def test_calculate_renko(calculator, sample_data):
    renko_chart = calculator.calculate_renko(sample_data, brick_size=2, chart_type='PERIOD_CLOSE')
    assert isinstance(renko_chart, pd.DataFrame)


def test_calculate_line_break(calculator, sample_data):
    line_break_chart = calculator.calculate_line_break(sample_data, line_number=3)
    assert isinstance(line_break_chart, pd.DataFrame)


def test_calculate_pnf(calculator, sample_data):
    pnf_chart = calculator.calculate_pnf(sample_data)
    assert isinstance(pnf_chart, pd.DataFrame)