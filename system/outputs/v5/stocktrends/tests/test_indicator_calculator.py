import pytest
import pandas as pd
from src.indicator_calculator import IndicatorCalculator

def test_calculate_renko():
    calculator = IndicatorCalculator()
    data = pd.DataFrame({'close': [100, 102, 104, 106, 108]})
    renko_data = calculator.calculate_renko(data, brick_size=2)
    assert len(renko_data) == 4


def test_calculate_line_break():
    calculator = IndicatorCalculator()
    data = pd.DataFrame({'close': [100, 102, 104, 106, 108]})
    line_break_data = calculator.calculate_line_break(data, line_count=3)
    assert len(line_break_data) == 5


def test_calculate_pnf():
    calculator = IndicatorCalculator()
    data = pd.DataFrame({'close': [100, 102, 104, 106, 108]})
    pnf_data = calculator.calculate_pnf(data)
    assert len(pnf_data) == 4