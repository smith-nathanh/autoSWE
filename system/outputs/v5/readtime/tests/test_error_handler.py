import pytest
from src.error_handler import ErrorHandler

class TestErrorHandler:
    def setup_method(self):
        self.error_handler = ErrorHandler()

    def test_validate_format_supported(self):
        try:
            self.error_handler.validate_format('plain_text')
        except ValueError:
            pytest.fail("validate_format raised ValueError unexpectedly!")

    def test_validate_format_unsupported(self):
        with pytest.raises(ValueError):
            self.error_handler.validate_format('unsupported')