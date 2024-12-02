import pytest
import pandas as pd
from src.indicator_calculator import IndicatorCalculator

@pytest.fixture
def calculator():
    return IndicatorCalculator()

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'close': [100, 102, 104, 106, 108, 110]
    })

def test_calculate_renko(calculator, sample_data):
    renko_data = calculator.calculate_renko(sample_data, brick_size=2)
    assert not renko_data.empty

def test_calculate_line_break(calculator, sample_data):
    line_break_data = calculator.calculate_line_break(sample_data, line_count=3)
    assert not line_break_data.empty

def test_calculate_pnf(calculator, sample_data):
    pnf_data = calculator.calculate_pnf(sample_data)
    assert not pnf_data.empty