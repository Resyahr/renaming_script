import os
from utils.file_operations import process_folder
from utils.console_output import print_separator, print_summary

def get_folder_path():
    """Prompt the user to enter the path to the folder to process."""
    while True:
        folder_path = input("Please enter the full path to the folder you want to process: ").strip()
        if os.path.isdir(folder_path):
            return folder_path
        else:
            print_separator()
            print(f"❌ Error: The path '{folder_path}' is not a valid directory. Please try again.")
            print_separator()

def main():
    print_separator()
    folder_path = get_folder_path()  # This will handle reading from config or asking the user if needed
    print_separator()

    summary = process_folder(folder_path)

    print_separator()
    print_summary(summary)

    print("\nPress any key to exit...")
    input()  # Wait for the user to press a key

if __name__ == "__main__":
    main()
