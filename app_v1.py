import streamlit as st
import os
from pdf_merger import PDFManipulator
from PyPDF2 import PdfReader
from typing import List, Tuple

def save_uploaded_file(uploaded_file, save_path: str) -> str:
    """Save uploaded file to disk and return the path"""
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return save_path

def main():
    st.set_page_config(page_title="PDF Manipulator", page_icon="📄")
    st.title("📄 PDF Manipulator")
    st.write("Merge PDFs or extract specific pages from a PDF")

    # Initialize session state for ranges if it doesn't exist
    if 'ranges' not in st.session_state:
        st.session_state.ranges = []

    # Create tabs for different operations
    tab1, tab2 = st.tabs(["Merge PDFs", "Extract Pages"])

    with tab1:
        st.header("Merge PDFs")
        st.write("Upload multiple PDF files to merge them into a single PDF")
        
        uploaded_files = st.file_uploader(
            "Choose PDF files to merge",
            type="pdf",
            accept_multiple_files=True
        )

        if uploaded_files and st.button("Merge PDFs"):
            try:
                # Create a temporary directory for uploaded files
                temp_dir = "temp_uploads"
                os.makedirs(temp_dir, exist_ok=True)
                
                # Save uploaded files
                input_files = []
                for uploaded_file in uploaded_files:
                    file_path = save_uploaded_file(
                        uploaded_file,
                        os.path.join(temp_dir, uploaded_file.name)
                    )
                    input_files.append(file_path)

                # Create output file path
                output_file = "merged_output.pdf"
                
                # Merge PDFs
                manipulator = PDFManipulator()
                manipulator.merge_pdfs(input_files, output_file)
                
                # Provide download link for the merged PDF
                with open(output_file, "rb") as f:
                    st.download_button(
                        label="Download Merged PDF",
                        data=f,
                        file_name="merged_output.pdf",
                        mime="application/pdf"
                    )
                
                # Clean up temporary files
                for file in input_files:
                    os.remove(file)
                os.rmdir(temp_dir)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")

    with tab2:
        st.header("Extract Pages")
        st.write("Upload a PDF file and specify the page ranges to extract")
        
        uploaded_file = st.file_uploader(
            "Choose a PDF file",
            type="pdf",
            key="segment_uploader"
        )

        if uploaded_file:
            try:
                # Save uploaded file
                temp_dir = "temp_uploads"
                os.makedirs(temp_dir, exist_ok=True)
                input_file = save_uploaded_file(
                    uploaded_file,
                    os.path.join(temp_dir, uploaded_file.name)
                )

                # Get PDF info
                reader = PdfReader(input_file)
                total_pages = len(reader.pages)
                st.write(f"Total pages in PDF: {total_pages}")

                # Page range input
                st.write("Enter page ranges to extract (0-based indexing)")
                
                col1, col2 = st.columns(2)
                with col1:
                    start_page = st.number_input("Start Page", 0, total_pages-1, 0)
                with col2:
                    end_page = st.number_input("End Page", 0, total_pages-1, 0)
                
                # Display current ranges
                if st.session_state.ranges:
                    st.write("Current ranges to extract:")
                    for start, end in st.session_state.ranges:
                        st.write(f"Pages {start} to {end}")

                col3, col4 = st.columns(2)
                with col3:
                    if st.button("Add Range"):
                        if start_page <= end_page:
                            st.session_state.ranges.append((start_page, end_page))
                            st.write(f"Added range: {start_page}-{end_page}")
                        else:
                            st.error("Start page must be less than or equal to end page")
                
                with col4:
                    if st.button("Clear Ranges"):
                        st.session_state.ranges = []
                        st.write("All ranges cleared")

                if st.session_state.ranges and st.button("Extract Pages"):
                    try:
                        output_file = "segmented_output.pdf"
                        manipulator = PDFManipulator()
                        manipulator.segment_pdf(input_file, output_file, st.session_state.ranges)
                        
                        # Provide download link for the segmented PDF
                        with open(output_file, "rb") as f:
                            st.download_button(
                                label="Download Segmented PDF",
                                data=f,
                                file_name="segmented_output.pdf",
                                mime="application/pdf"
                            )
                        
                        # Clean up temporary files
                        os.remove(input_file)
                        os.rmdir(temp_dir)
                        
                    except Exception as e:
                        st.error(f"Error: {str(e)}")

            except Exception as e:
                st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 