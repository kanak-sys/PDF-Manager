from PyPDF2 import PdfMerger
import os

def merge_pdfs():
    merger = PdfMerger()
    files = input("Enter the PDF file names to merge separated by commas: ").split(',')

    for file in files:
        file = file.strip()
        if os.path.exists(file):
            merger.append(file)
        else:
            print(f"File not found: {file}")

    output = input("Enter the name of the output file (e.g., merged.pdf): ")
    merger.write(output)
    merger.close()
    print(f"Merged PDF saved as {output}")
