from PyPDF2 import PdfReader, PdfWriter

def cut_pdf_pages():
    path = input("Enter the PDF file name to select pages from: ")
    reader = PdfReader(path)
    writer = PdfWriter()

    print(f"The PDF has {len(reader.pages)} pages.")
    pages = input("Enter the page numbers to extract (comma-separated, 0-indexed): ").split(',')

    for p in pages:
        try:
            writer.add_page(reader.pages[int(p.strip())])
        except Exception as e:
            print(f"Error adding page {p.strip()}: {e}")

    output = input("Enter the name of the new PDF file: ")
    with open(output, "wb") as f:
        writer.write(f)
    print(f"Selected pages merged into {output}")
