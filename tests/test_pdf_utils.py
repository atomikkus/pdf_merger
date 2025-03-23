import unittest
import os
from src.utils.pdf_utils import PDFManipulator
from src.config.settings import TEMP_DIR, OUTPUT_DIR

class TestPDFManipulator(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.manipulator = PDFManipulator()
        
    def tearDown(self):
        """Clean up after each test method."""
        # Clean up any test files
        for dir_path in [TEMP_DIR, OUTPUT_DIR]:
            for file in os.listdir(dir_path):
                file_path = os.path.join(dir_path, file)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                except Exception as e:
                    print(f"Error: {e}")

    def test_merge_pdfs(self):
        """Test PDF merging functionality."""
        # Add your test implementation here
        pass

    def test_segment_pdf(self):
        """Test PDF segmentation functionality."""
        # Add your test implementation here
        pass

if __name__ == '__main__':
    unittest.main() 