import os
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from typing import List, Union, Tuple

class PDFManipulator:
    def __init__(self):
        self.merger = PdfMerger()
        self.reader = None
        self.writer = PdfWriter()

    def merge_pdfs(self, input_files: List[str], output_file: str) -> None:
        """
        Merge multiple PDF files into a single PDF.
        
        Args:
            input_files (List[str]): List of paths to input PDF files
            output_file (str): Path to the output PDF file
        """
        try:
            for pdf in input_files:
                if not os.path.exists(pdf):
                    raise FileNotFoundError(f"File not found: {pdf}")
                self.merger.append(pdf)
            
            self.merger.write(output_file)
            self.merger.close()
            print(f"Successfully merged PDFs into: {output_file}")
        except Exception as e:
            print(f"Error merging PDFs: {str(e)}")
            self.merger.close()

    def segment_pdf(self, input_file: str, output_file: str, 
                   page_ranges: List[Tuple[int, int]]) -> None:
        """
        Extract specific page ranges from a PDF file.
        
        Args:
            input_file (str): Path to the input PDF file
            output_file (str): Path to the output PDF file
            page_ranges (List[Tuple[int, int]]): List of (start_page, end_page) tuples
                                               (0-based indexing)
        """
        try:
            if not os.path.exists(input_file):
                raise FileNotFoundError(f"File not found: {input_file}")

            reader = PdfReader(input_file)
            writer = PdfWriter()

            for start, end in page_ranges:
                if start < 0 or end >= len(reader.pages):
                    raise ValueError(f"Invalid page range: {start}-{end}")
                
                for page_num in range(start, end + 1):
                    writer.add_page(reader.pages[page_num])

            with open(output_file, 'wb') as output:
                writer.write(output)
            
            print(f"Successfully segmented PDF into: {output_file}")
        except Exception as e:
            print(f"Error segmenting PDF: {str(e)}")

def main():
    # Example usage
    manipulator = PDFManipulator()
    
    # Example for merging PDFs
    input_files = ["file1.pdf", "file2.pdf"]
    output_file = "merged_output.pdf"
    manipulator.merge_pdfs(input_files, output_file)
    
    # Example for segmenting PDF
    input_file = "input.pdf"
    output_file = "segmented_output.pdf"
    page_ranges = [(0, 2), (5, 7)]  # Extract pages 0-2 and 5-7
    manipulator.segment_pdf(input_file, output_file, page_ranges)

if __name__ == "__main__":
    main() 