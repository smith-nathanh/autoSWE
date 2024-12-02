from src.read_time_calculator import ReadTimeCalculator

if __name__ == "__main__":
    calculator = ReadTimeCalculator()

    # Example with plain text
    plain_text = "This is a simple plain text example."
    processed_text = calculator.process_content(plain_text, "plain_text")
    reading_time = calculator.calculate_reading_time(processed_text)
    print(f"Estimated reading time for plain text: {reading_time:.2f} minutes")

    # Example with HTML
    html_content = "<p>This is a simple HTML example.</p>"
    processed_html = calculator.process_content(html_content, "html")
    reading_time = calculator.calculate_reading_time(processed_html)
    print(f"Estimated reading time for HTML: {reading_time:.2f} minutes")

    # Example with Markdown
    markdown_content = "# This is a simple markdown example."
    processed_markdown = calculator.process_content(markdown_content, "markdown")
    reading_time = calculator.calculate_reading_time(processed_markdown)
    print(f"Estimated reading time for Markdown: {reading_time:.2f} minutes")