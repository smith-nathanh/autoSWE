class ErrorHandler:
    def validate_format(self, format: str):
        supported_formats = ['plain_text', 'html', 'markdown']
        if format not in supported_formats:
            self.handle_unsupported_format(format)

    def handle_unsupported_format(self, format: str):
        raise ValueError(f"Unsupported format: {format}")