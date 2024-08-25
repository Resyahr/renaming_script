import os
from datetime import datetime
from utils.pdf_processing import read_pdf_information, open_file_for_review, standardize_date
from utils.input_validation import get_validated_inputs
from utils.console_output import print_separator, print_success, print_skip, print_error, print_prompt

# Path to the log file
LOG_FILE_PATH = 'processed_files.log'


def load_processed_files():
    """Load the list of already processed files from the log file."""
    if os.path.exists(LOG_FILE_PATH):
        with open(LOG_FILE_PATH, 'r') as log_file:
            processed_files = log_file.read().splitlines()
    else:
        processed_files = []
    return set(processed_files)


def save_processed_file(filename):
    """Save a file as processed by appending it to the log file."""
    with open(LOG_FILE_PATH, 'a') as log_file:
        log_file.write(filename + '\n')


def sanitize_filename(name):
    name = name.replace('/', '-').replace(' ', '')
    first_hyphen_index = name.find('-')
    if first_hyphen_index != -1:
        name = name[:first_hyphen_index]
    return name


def extract_date_from_filename(filename):
    """Extract the date from the filename in the format ddmmyyyy-hhmmss."""
    try:
        base_name = os.path.splitext(filename)[0]
        date_part = base_name.split('_')[-1]  # Extract the part after the underscore
        date_str = date_part[:8]  # The date part is the first 8 characters (ddmmyyyy)
        return datetime.strptime(date_str, "%d%m%Y").strftime("%d.%m.%Y")
    except Exception as e:
        print(f"❌ Error extracting date from filename {filename}: {e}")
        return None


def rename_pdf(file_path, tool_description, tool_serial_number, report_date):
    directory, original_filename = os.path.split(file_path)
    new_filename = f"MFU_{tool_description}_{tool_serial_number}_{report_date}.pdf"
    new_file_path = os.path.join(directory, new_filename)
    os.rename(file_path, new_file_path)
    return original_filename, new_filename


def process_folder(folder_path):
    print_separator()
    print(f"\nProcessing folder: {folder_path}\n")

    # Initialize counters
    success_count = 0
    skipped_count = 0
    error_count = 0
    error_files = []

    # Load already processed files
    processed_files = load_processed_files()

    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            if filename in processed_files:
                print_skip(filename)
                skipped_count += 1
                continue

            print_separator()
            file_path = os.path.join(folder_path, filename)
            print(f"\nProcessing file: {filename}")

            # Extract info from the PDF
            tool_description, tool_serial_number, report_date = read_pdf_information(file_path)

            if report_date:
                report_date = standardize_date(report_date)

            if tool_description and tool_serial_number and report_date:
                try:
                    original_filename, renamed_filename = rename_pdf(file_path, tool_description, tool_serial_number,
                                                                     report_date)
                    success_count += 1
                    print_success(original_filename, renamed_filename)
                except Exception as e:
                    error_count += 1
                    error_files.append(filename)
                    print_error(filename, str(e))
            else:
                error_count += 1
                error_files.append(filename)
                print_error(filename, "missing required information")
                open_file_for_review(file_path)

            save_processed_file(filename)
        else:
            continue

    print_separator()

    # Return a summary of the operation
    return {
        'renamed': success_count,
        'skipped': skipped_count,
        'errors': error_count,
        'error_files': error_files
    }
