# AI Document Summarizer

## Overview

AI Document Summarizer is a Python desktop application that uses advanced natural language processing to generate concise summaries of PDF documents. Leveraging the power of Hugging Face's Transformers library, this tool provides quick and accurate text summaries with just a few clicks.

## Features

- 📄 PDF Text Extraction
- 🤖 AI-Powered Summarization
- 🖥️ Simple, User-Friendly GUI
- 📋 Customizable Summary Length

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.8+
- tkinter
- transformers
- PyPDF2

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-document-summarizer.git
   cd ai-document-summarizer
   ```

2. Install required dependencies:
   ```bash
   pip install transformers PyPDF2 torch
   ```

## Usage

1. Run the application:
   ```bash
   python pdf_summarizer.py
   ```

2. Click "Select PDF File"
3. Choose a PDF document
4. View the AI-generated summary in the text box

## Customization

You can modify summary parameters in the `summarize_text()` function:
- `max_length`: Maximum summary length (default: 150)
- `min_length`: Minimum summary length (default: 30)

## Technologies

- Python
- tkinter
- Transformers (BART model)
- PyPDF2

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- [Hugging Face Transformers](https://github.com/huggingface/transformers)
- [PyPDF2](https://github.com/py-pdf/PyPDF2)

## Contact

Your Name - youremail@example.com

Project Link: [https://github.com/yourusername/ai-document-summarizer](https://github.com/yourusername/ai-document-summarizer)
