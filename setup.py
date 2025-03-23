from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pdf-manipulator",
    version="0.1.0",
    author="Satya",
    author_email="sprakashk2896@gmail.com",
    description="A tool for merging and extracting pages from PDF files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atomikkus/pdf-manipulator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "PyPDF2==3.0.1",
        "streamlit==1.32.0",
        "typing-extensions>=4.5.0",
        "python-dateutil>=2.8.2",
        "pytz>=2023.3",
        "six>=1.16.0",
    ],
    entry_points={
        "console_scripts": [
            "pdf-manipulator=src.app:main",
        ],
    },
) 
