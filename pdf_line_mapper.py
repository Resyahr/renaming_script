import PyPDF2


def extract_lines_from_pdf(path_to_file):
    """Extracts all lines of text from a PDF file and prints them with their corresponding indices."""
    with open(path_to_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        page = reader.pages[1]  # Assuming the information is on the second page
        text = page.extract_text()

    # Split the text into lines
    lines = text.splitlines()

    # Print each line with its index
    for index, line in enumerate(lines):
        print(f"Line {index}: {line}")


if __name__ == "__main__":
    # Path to the PDF file in the root directory
    pdf_path = "file_to_rename_1.pdf"

    extract_lines_from_pdf(pdf_path)
