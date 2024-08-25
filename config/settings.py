import os

# Path to the config file
CONFIG_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'config.txt')

def get_folder_path():
    """Retrieve or set the folder path for processing."""
    if os.path.exists(CONFIG_FILE_PATH):
        # Read the folder path from the config file
        with open(CONFIG_FILE_PATH, 'r') as config_file:
            folder_path = config_file.readline().strip()
            if os.path.isdir(folder_path):
                print(f"Using folder path from config file: {folder_path}")
                return folder_path
            else:
                print("Invalid folder path in config file. Please provide a new one.")
    else:
        print("Config file not found. Please provide the folder path.")

    # Prompt user for the folder path
    folder_path = input("Enter the full path to the folder containing the PDF files: ").strip()

    # Validate the folder path
    if os.path.isdir(folder_path):
        # Write the folder path to the config file
        with open(CONFIG_FILE_PATH, 'w') as config_file:
            config_file.write(folder_path)
            print(f"Folder path saved to config file: {folder_path}")
        return folder_path
    else:
        print("Invalid folder path. Please check the path and try again.")
        return None
