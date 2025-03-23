# PDF Manipulator

A powerful and user-friendly web application for PDF manipulation tasks. Built with Python, Streamlit, and PyPDF2, this tool allows you to merge multiple PDFs and extract specific page ranges with ease.

## Features

- 📄 Merge multiple PDF files into a single PDF
- ✂️ Extract specific page ranges from a PDF
- 🎯 Create separate PDFs for each extracted range
- 📦 Download individual PDFs or all extracts as a ZIP file
- 🌐 User-friendly web interface
- 🔄 Clean temporary files automatically
- 🛡️ Error handling and validation
- 📱 Responsive design

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Git (optional, for cloning)

### Quick Install
1. Clone this repository:
```bash
git clone https://github.com/yourusername/pdf-manipulator.git
cd pdf-manipulator
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Development Install
For developers who want to contribute or modify the code:
```bash
pip install -e .
```

## Usage

### Starting the Application
1. Start the Streamlit web application:
```bash
streamlit run src/app.py
```

2. Open your web browser and navigate to the provided URL (typically http://localhost:8501)

### Merging PDFs

1. Select the "Merge PDFs" tab
2. Upload multiple PDF files using the file uploader
3. Click "Merge PDFs"
4. Download the merged PDF file

### Extracting Pages

1. Select the "Extract Pages" tab
2. Upload a PDF file
3. Add page ranges to extract:
   - Enter start and end page numbers (0-based indexing)
   - Click "Add Range" (repeat for multiple ranges)
4. Click "Extract Pages"
5. Choose to either:
   - Download individual PDFs separately
   - Download all extracted PDFs as a ZIP file

### Important Notes
- Page numbers are 0-based (first page is 0)
- Maximum file size: 200MB per file
- Supported format: PDF only
- Temporary files are automatically cleaned up

## Project Structure

```
pdf-manipulator/
├── src/                # Source code directory
│   ├── app.py         # Main Streamlit application
│   ├── utils/         # Utility functions and helpers
│   │   ├── __init__.py
│   │   └── pdf_utils.py  # PDF manipulation logic
│   └── config/        # Configuration files
│       ├── __init__.py
│       └── settings.py   # Application settings
├── tests/             # Test files
│   ├── __init__.py
│   └── test_pdf_utils.py
├── docs/              # Documentation
│   └── README.md      # Detailed documentation
├── data/              # Data directory
│   ├── temp/          # Temporary files
│   └── output/        # Output files
├── requirements.txt   # Python dependencies
├── setup.py          # Package setup file
├── LICENSE           # MIT License
└── README.md         # Project documentation
```

## Dependencies

- Python 3.7+
- Streamlit (1.32.0)
- PyPDF2 (3.0.1)
- Other dependencies listed in requirements.txt

## Development

### Running Tests
```bash
python -m unittest discover tests
```

### Code Style
We follow PEP 8 guidelines for Python code. Before submitting a pull request:
1. Format your code
2. Run the test suite
3. Check for any linting errors

## Troubleshooting

### Common Issues
1. **"NoneType object is not callable" error**
   - Make sure you're using the correct version of PyPDF2
   - Try reinstalling the dependencies

2. **File not found errors**
   - Check if the data/temp and data/output directories exist
   - Ensure you have write permissions

3. **Memory errors with large PDFs**
   - Try splitting the task into smaller batches
   - Check available system memory

### Getting Help
If you encounter any issues:
1. Check the [Issues](https://github.com/yourusername/pdf-manipulator/issues) page
2. Search for similar problems
3. Create a new issue with:
   - Description of the problem
   - Steps to reproduce
   - Error message
   - System information

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Review Process
1. Ensure all tests pass
2. Follow the code style guidelines
3. Update documentation if needed
4. Add tests for new features

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- PDF processing powered by [PyPDF2](https://pypdf2.readthedocs.io/)
- Thanks to all contributors who have helped shape this project

## Version History

- 0.1.0
  - Initial release
  - Basic PDF merging and extraction features
  - Streamlit web interface 