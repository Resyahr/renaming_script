from colorama import Fore, Back, Style

def print_separator():
    print("-" * 100 + Style.RESET_ALL)

def print_success(original_filename, renamed_filename):
    print(Back.LIGHTGREEN_EX + Fore.BLACK + "☑️ File renamed from " +
          Fore.BLACK + original_filename + Fore.BLACK + " → " +
          Fore.BLACK + renamed_filename + Style.RESET_ALL)

def print_skip(filename):
    print(Back.LIGHTWHITE_EX + Fore.BLACK + f"⏩ Skipped: {filename} (already formatted correctly)\n" + Style.RESET_ALL)

def print_error(filename, error_message):
    print(Back.RED + Fore.LIGHTWHITE_EX + f"✖️ Error renaming file {filename}: {error_message}\n" + Style.RESET_ALL)

def print_prompt(input_type, example):
    while True:
        try:
            user_input = input(Back.LIGHTWHITE_EX + Fore.BLACK + f"Please enter the {input_type} ({example}): " + Style.RESET_ALL)
            return user_input
        except ValueError as ve:
            print(Back.RED + Fore.WHITE + str(ve) + Style.RESET_ALL)

def print_summary(summary):
    print(Back.LIGHTWHITE_EX + Fore.BLACK + "Summary:" + Style.RESET_ALL)
    print(Back.LIGHTGREEN_EX + Fore.BLACK + f"☑️ Successfully renamed: {summary.get('renamed', 0)} files" + Style.RESET_ALL)
    print(Back.LIGHTWHITE_EX + Fore.BLACK + f"⏩ Skipped (already formatted): {summary.get('skipped', 0)} files" + Style.RESET_ALL)
    if summary.get('errors', 0) > 0:
        print(Back.RED + Fore.LIGHTWHITE_EX + f"✖️ Errors in: {summary.get('errors', 0)} files" + Style.RESET_ALL)