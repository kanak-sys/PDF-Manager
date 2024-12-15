# PDF Manager Application

## Overview
The **PDF Manager Application** provides tools to manage, merge, extract images, and cut PDF files. This CLI-based application offers three main functionalities:

1. **Merge PDFs**: Allows users to merge multiple PDF files into a single document.
2. **Extract Images from PDFs**: Extracts images from all pages of a PDF and saves them to the local system.
3. **Merge PDFs by Pages**: Allows users to merge specific pages from a PDF file into a new document.

## Features
- **Merge PDFs**: Combine multiple PDFs into one PDF document.
- **Extract Images**: Extract images from a PDF and save them as individual image files (e.g., PNG).
- **Merge PDFs by Pages**: Select and merge specific pages from a PDF into a new file.
- **Easy-to-use Command Line Interface**: Navigate through the application using simple menu options.

## Tools and Technologies
- Python
- `PyPDF2` for PDF operations (merging, cutting, etc.)
- File handling for image extraction
- `os` and `datetime` for managing file paths and timestamps

## Installation
1. Clone or download the repository.
2. Install Python (if not already installed).
3. Install required libraries by running:
    ```bash
    pip install PyPDF2
    ```
   
## How to Use
1. Clone or download the repository.
2. Navigate to the directory where the Python files are located.
3. Run the `main.py` file using:
    ```bash
    python main.py
    ```
4. Select an option from the menu:
    - **1**: Merge PDFs - Enter the paths of the PDFs to merge.
    - **2**: Extract Images from PDF - Enter the path of the PDF to extract images.
    - **3**: Merge PDFs by Pages - Select pages from a PDF to merge.
    - **4**: Exit - Close the application.

### Example Menu
Welcome to the PDF Manager Application!

What is your Purpose:

Merge PDFs
Extract Images from PDF
Merge PDFs by Pages
Exit Enter your choice (1-4): 1
