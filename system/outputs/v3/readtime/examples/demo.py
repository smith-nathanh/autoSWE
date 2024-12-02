from src.read_time_calculator import ReadTimeCalculator

if __name__ == "__main__":
    calculator = ReadTimeCalculator()
    
    # Sample content
    plain_text = open('samples/plain_text.txt').read()
    html_content = open('samples/html.html').read()
    markdown_content = open('samples/markdown.md').read()

    # Calculate reading time for each format
    print("Plain Text Reading Time:", calculator.process_content(plain_text, 'plain_text'))
    print("HTML Reading Time:", calculator.process_content(html_content, 'html'))
    print("Markdown Reading Time:", calculator.process_content(markdown_content, 'markdown'))
