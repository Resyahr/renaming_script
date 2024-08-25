import os
import PyPDF2
import subprocess

def extract_specific_lines(text):
    lines = text.splitlines()
    try:
        # For German version
        if 'Bericht Datum' in lines[105]:
            report_date = lines[111].strip()
            tool_description = lines[115].strip()
            tool_serial_number = lines[116].strip()
        # For English version
        elif 'Report date' in lines[102]:
            report_date = lines[108].strip()
            tool_description = lines[112].strip()
            tool_serial_number = lines[113].strip()

        # Sanitize tool description by keeping only the part before the slash
        if '/' in tool_description:
            tool_description = tool_description.split('/')[0].strip()

        # Print extracted data for verification
        print(f"Extracted - Tool Description: {tool_description}, Serial Number: {tool_serial_number}, Report Date: {report_date}")

        return tool_description, tool_serial_number, report_date
    except IndexError as e:
        print(f"❌ Error processing lines: {e}")
        return None, None, None



def standardize_date(date_str):
    from datetime import datetime

    for fmt in ("%d.%m.%Y", "%m/%d/%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(date_str, fmt).strftime("%d.%m.%Y")
        except ValueError:
            continue
    return None  # If none of the formats match, return None


def read_pdf_information(path_to_file):
    with open(path_to_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        page = reader.pages[1]
        text = page.extract_text()
    return extract_specific_lines(text)

def open_file_for_review(file_path):
    try:
        if not os.path.exists(file_path):
            print(f"❌ File not found: {file_path}")
            return

        pdf_viewer_path = r'C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe'
        subprocess.run([pdf_viewer_path, file_path], check=True)
    except Exception as e:
        print(f"❌ Failed to open file {file_path} for review: {str(e)}")
