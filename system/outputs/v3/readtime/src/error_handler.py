class ErrorHandler:
    def validate_input(self, content: str, format: str):
        if not content or not format:
            raise ValueError("Content and format must be provided.")

    def handle_unsupported_format(self, format: str):
        return f"Error: Unsupported format '{format}'. Supported formats are plain_text, html, markdown."
