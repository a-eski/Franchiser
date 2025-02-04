"""
Franchiser: Downloading and processing Financial Disclosure Documents (FDD's) for academic purposes.
Copyright (C) 2025 Alex Eski <alexeski at gmail dot com>

This file extracts franchises from a Franchises Index PDF. Data requires being cleaned up afterwords.

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

print('Franchiser PDF Extractor started')

i = 1
current_file = 'RawData/franchises_index_'
with open('RawData/Franchises.pdf', 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file, False)
        for page_num in range(len(reader.pages)):
            text = reader.pages[page_num].extract_text().replace('\u2264', '')
            print(text)
            with open(current_file + str(i) + '.txt', "w") as file:
                file.write(text)
                i += 1

print('Franchiser PDF Extractor finished')
