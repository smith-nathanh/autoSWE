class ErrorHandler:
    def validate_input(self, content: str, format: str):
        if not content or not format:
            raise ValueError("Content and format must be provided.")

    def raise_unsupported_format_error(self, format: str):
        raise ValueError(f"Unsupported format: {format}")