import os
from src.read_time_calculator import ReadTimeCalculator

# Sample file paths
SAMPLES_DIR = os.path.join(os.path.dirname(__file__), '../samples')
HTML_FILE = os.path.join(SAMPLES_DIR, 'html.html')
MARKDOWN_FILE = os.path.join(SAMPLES_DIR, 'markdown.md')
PLAIN_TEXT_FILE = os.path.join(SAMPLES_DIR, 'plain_text.txt')

# Function to read file content
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Main function to demonstrate reading time estimation
def main():
    calculator = ReadTimeCalculator()
    
    # Read and estimate reading time for HTML content
    html_content = read_file(HTML_FILE)
    html_reading_time = calculator.estimate_reading_time(html_content, calculator.default_wpm)
    print(f"Estimated reading time for HTML content: {html_reading_time} minutes")

    # Read and estimate reading time for Markdown content
    markdown_content = read_file(MARKDOWN_FILE)
    markdown_reading_time = calculator.estimate_reading_time(markdown_content, calculator.default_wpm)
    print(f"Estimated reading time for Markdown content: {markdown_reading_time} minutes")

    # Read and estimate reading time for Plain Text content
    plain_text_content = read_file(PLAIN_TEXT_FILE)
    plain_text_reading_time = calculator.estimate_reading_time(plain_text_content, calculator.default_wpm)
    print(f"Estimated reading time for Plain Text content: {plain_text_reading_time} minutes")

if __name__ == "__main__":
    main()