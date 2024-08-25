from colorama import Fore, Back, Style
import re

def is_valid_tool_description(description):
    return re.match(r'^[A-Z]{1,2}[0-9]{3}$', description) is not None

def is_valid_tool_serial_number(serial_number):
    return re.match(r'^[A-Z][0-9]{7}$', serial_number) is not None

def is_valid_report_date(date):
    return re.match(r'^\d{2}\.\d{2}\.\d{4}$', date) is not None

def get_validated_inputs():
    while True:
        tool_description = input(Back.RED + Fore.WHITE + "Please enter the Tool Description (e.g., B006): " + Style.RESET_ALL).strip()
        tool_serial_number = input(Back.RED + Fore.WHITE + "Please enter the Tool S.N (e.g., A3671293): " + Style.RESET_ALL).strip()
        report_date = input(Back.RED + Fore.WHITE + "Please enter the Report date (dd.mm.yyyy): " + Style.RESET_ALL).strip()

        if is_valid_tool_description(tool_description) and is_valid_tool_serial_number(tool_serial_number) and is_valid_report_date(report_date):
            return tool_description, tool_serial_number, report_date
        else:
            print(Back.RED + Fore.WHITE + "Error: One or more inputs are invalid. Please enter the correct values." + Style.RESET_ALL)
