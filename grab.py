import os
from openpyxl import Workbook
from openpyxl.utils.exceptions import IllegalCharacterError

def read_text_files_and_create_excel(root_directory, excel_file_path):
    wb = Workbook()
    ws = wb.active
    
    for root, dirs, files in os.walk(root_directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-16le') as f:
                    content = f.read()
                # Replace illegal characters with an empty string
                content = remove_illegal_characters(content)
                try:
                    ws.append([content])
                except IllegalCharacterError as e:
                    print(f"Illegal characters encountered in file: {file_path}. Skipping...")
                    print(f"Error message: {e}")
                
    wb.save(excel_file_path)

def remove_illegal_characters(content):
    # Replace illegal characters with an empty string
    illegal_characters = ['#', '♠', '/']
    for char in illegal_characters:
        content = content.replace(char, '')
    return content

# Example usage
root_directory = r'C:\translationenviroment\arabic 4.0\Extracted\Mechanics\Spells\Bard'
excel_file_path = r'C:\arabic 4.0\bard.xlsx'
read_text_files_and_create_excel(root_directory, excel_file_path)
