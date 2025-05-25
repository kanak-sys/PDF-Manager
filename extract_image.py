from pdf2image import convert_from_path
import os

def extract_images_from_pdf():
    pdf_path = input("Enter the path to the PDF file: ")
    output_folder = "extracted_images"
    os.makedirs(output_folder, exist_ok=True)

    try:
        pages = convert_from_path(pdf_path)
        for i, page in enumerate(pages):
            image_path = os.path.join(output_folder, f"page_{i+1}.png")
            page.save(image_path, "PNG")
            print(f"Saved {image_path}")
    except Exception as e:
        print(f"Error extracting images: {e}")
