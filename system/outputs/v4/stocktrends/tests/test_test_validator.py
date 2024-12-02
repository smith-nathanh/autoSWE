import pytest
import pandas as pd
from src.test_validator import TestValidator

@pytest.fixture
def validator():
    return TestValidator()

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'close': [100, 102, 104, 106, 108, 110]
    })

@pytest.fixture
def expected_data():
    return pd.DataFrame({
        'close': [100, 102, 104, 106, 108, 110]
    })

def test_validate_renko(validator, sample_data, expected_data):
    assert validator.validate_renko(sample_data, expected_data)


def test_validate_line_break(validator, sample_data, expected_data):
    assert validator.validate_line_break(sample_data, expected_data)