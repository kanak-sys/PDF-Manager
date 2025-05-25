from merge_pdfs import merge_pdfs
from Cutter_PDF import cut_pdf_pages
from extract_image import extract_images_from_pdf

def main():
    while True:
        print("\nWelcome to the PDF Manager Application!\n")
        print("What is your Purpose:\n")
        print("1. Merge PDFs")
        print("2. Extract Images from PDF")
        print("3. Merge PDFs by Pages")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            merge_pdfs()
        elif choice == '2':
            extract_images_from_pdf()
        elif choice == '3':
            cut_pdf_pages()
        elif choice == '4':
            print("Thank you for using PDF Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
