# This is a sample Python script.
from NLP import format_page

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


if __name__ == "__main__":
    input_text = """
    Natural language processing (NLP) is a field of artificial intelligence that focuses on the interaction 
    between computers and humans through natural language. It enables computers to understand, interpret, 
    and generate human-like text.

    Tokenization is the process of breaking down text into words or phrases, known as tokens. In NLP, 
    tokenization is a crucial step in various applications, including sentiment analysis, language translation, 
    and text summarization.

    Stopwords are common words that do not carry much meaning and are often removed during text processing. 
    Examples of stopwords include "the," "and," and "is."

    This is a simple page formatter using natural language processing in Python. It identifies headings 
    and regular paragraphs in the input text and formats them accordingly.
    """

    formatted_output = format_page(input_text)
    print(formatted_output)
