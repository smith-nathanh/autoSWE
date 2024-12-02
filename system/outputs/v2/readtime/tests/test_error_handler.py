import pytest
from src.error_handler import ErrorHandler

@pytest.fixture
def error_handler():
    return ErrorHandler()


def test_validate_input(error_handler):
    with pytest.raises(ValueError, match="Content and format must be provided."):
        error_handler.validate_input("", "plain_text")


def test_raise_unsupported_format_error(error_handler):
    with pytest.raises(ValueError, match="Unsupported format: xml"):
        error_handler.raise_unsupported_format_error("xml")