"""
Franchiser: Downloading and processing Financial Disclosure Documents (FDD's) for academic purposes.
Copyright (C) 2025 Alex Eski <alexeski at gmail dot com>

This file extracts issuance year from FDDs and appends the file name with the issuance year.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import PyPDF2
import os

def get_issuance_line_in_pdf(file):
    with open(file, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file, False)
        for page_num in range(len(reader.pages)):
            text = reader.pages[page_num].extract_text()
            if 'Date of Issuance' in text:
                lines = text.replace('.', '').split('\n')
                for line in lines:
                    if 'Date of Issuance' in line:
                        return line
            if 'Issuance Date' in text:
                lines = text.replace('.', '').split('\n')
                for line in lines:
                    if 'Issuance Date' in line:
                        return line
            elif 'issuance' in text:
                lines = text.replace('.', '').split('\n')
                for line in lines:
                    if 'issuance' in line:
                        return line
            elif 'Issuance' in text:
                lines = text.replace('.', '').split('\n')
                for line in lines:
                    if 'Issuance' in line:
                        return line
            elif 'ISSUANCE' in text:
                lines = text.replace('.', '').split('\n')
                for line in lines:
                    if 'ISSUANCE' in line:
                        return line
    return ""

def int_convert(str):
    try:
        return int(str)
    except ValueError:
        return 0

def get_issuance_year(file):
    issuance_line = get_issuance_line_in_pdf(file)
    if issuance_line == "":
        return "Line not found";
    # print(issuance_line);
    split_line = issuance_line.replace(':', '').split(' ')
    for element in split_line:
        if len(element) != 4:
            last_four = element[-4:]
            element_int = int_convert(last_four)
            if 2000 <= element_int <= 2100:
                return last_four
            continue
        element_int = int_convert(element)
        if 2000 <= element_int <= 2100:
            return element

    line = issuance_line.replace(' ', '').replace(',', '')
    line = line.replace('.', '').replace(':', '')
    line = line.replace('l', '1').replace('®', '')
    line = line.replace("'", '').replace('-', '')
    line = line.replace('_', '').replace('*', '')[-4:]
    print(line);
    element_int = int_convert(line)
    if 2000 <= element_int <= 2100:
        return line

    return "Year not found"

def rename_file(file, new_name):
    try:
        os.rename(file, new_name)
    except Exception as e:
        print(f"Error occured while renaming file {file}: {e}")

def rename_fdd_file(directory, file, issuance_year):
    new_name = issuance_year + '_' + file
    print('Renaming ' + file +' to ' + new_name)
    rename_file(directory + file, directory + new_name)

print('Franchiser PDF Renamer started')

directory = 'Data/'
files = os.listdir(directory)

for file in files:
    file_path = directory + file
    issuance_year = get_issuance_year(file_path)

    if issuance_year == "Line not found":
        print('No issuance line found for ' + file)
        continue
    elif issuance_year == "Year not found":
        print ('No issuance year found in issuance line for ' + file)
        continue

    rename_fdd_file(directory, file, issuance_year)

print('Franchiser PDF Renamer finished')
