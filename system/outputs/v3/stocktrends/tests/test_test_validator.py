import pytest
from src.test_validator import TestValidator

@pytest.fixture
def validator():
    return TestValidator()


def test_run_unit_tests(validator):
    # This test will run all unit tests
    validator.run_unit_tests()


def test_run_acceptance_tests(validator):
    # Placeholder for acceptance test execution
    validator.run_acceptance_tests()