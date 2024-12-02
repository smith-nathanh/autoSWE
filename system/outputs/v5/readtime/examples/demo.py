from src.read_time_calculator import ReadTimeCalculator

if __name__ == "__main__":
    calculator = ReadTimeCalculator()
    
    # Example with plain text
    with open('samples/plain_text.txt', 'r') as file:
        content = file.read()
    processed_content = calculator.process_content(content, 'plain_text')
    reading_time = calculator.calculate_reading_time(processed_content)
    print(f"Estimated reading time for plain text: {reading_time:.2f} minutes")

    # Example with HTML
    with open('samples/html.html', 'r') as file:
        content = file.read()
    processed_content = calculator.process_content(content, 'html')
    reading_time = calculator.calculate_reading_time(processed_content)
    print(f"Estimated reading time for HTML: {reading_time:.2f} minutes")

    # Example with Markdown
    with open('samples/markdown.md', 'r') as file:
        content = file.read()
    processed_content = calculator.process_content(content, 'markdown')
    reading_time = calculator.calculate_reading_time(processed_content)
    print(f"Estimated reading time for Markdown: {reading_time:.2f} minutes")