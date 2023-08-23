import os
from PyPDF2 import PdfReader, PdfWriter


def get_user_input():
    pdf_file_name = input("Enter the master PDF file name (without extension): ")
    chunk_size = input("Enter the number of pages per file (e.g., 8): ")
    output_folder = input(
        "Enter the output folder name (create a new folder if needed): "
    )
    output_filename = input("Enter the base file name (e.g., file): ")
    return pdf_file_name, int(chunk_size), output_folder, output_filename


def split_pdf(pdf_file_name, chunk_size, output_folder, output_filename):
    pdf_file_path = os.path.join(os.getcwd(), f"{pdf_file_name}.pdf")
    output_folder_path = os.path.join(os.getcwd(), output_folder)

    if not os.path.exists(pdf_file_path):
        print(f"Error: Master PDF file '{pdf_file_name}.pdf' not found.")
        return

    os.makedirs(output_folder_path, exist_ok=True)
    pdf = PdfReader(pdf_file_path)

    total_pages = len(pdf.pages)
    chunk_number = 1
    for start_page in range(0, total_pages, chunk_size):
        end_page = min(start_page + chunk_size, total_pages)
        chunk_pdf = PdfWriter()
        for page_number in range(end_page - 1, start_page - 1, -1):
            chunk_pdf.insert_page(pdf.pages[page_number])
        chunk_file_name = f"{output_filename}_{chunk_number}.pdf"  # Format chunk number with leading zeros
        chunk_file_path = os.path.join(output_folder_path, chunk_file_name)
        with open(chunk_file_path, "wb") as chunk_file:
            chunk_pdf.write(chunk_file)
            print(f"{os.path.basename(chunk_file_path)} berhasil disimpan")
        chunk_number += 1

    print("Splitting complete.")


def main():
    print("Welcome to the PDF Splitter!")
    pdf_file_name, chunk_size, output_folder, output_filename = get_user_input()
    split_pdf(pdf_file_name, chunk_size, output_folder, output_filename)


if __name__ == "__main__":
    main()
