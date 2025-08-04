import os.path
from zipfile import ZipFile

with ZipFile("workbook.zip") as zip_file:
    files_size = 0
    compress_size = 0

    koef_list = []

    for info in zip_file.infolist():
        if not info.is_dir() and info.file_size > 0:

            koef_list.append(((info.compress_size/info.file_size)*100, info.filename))
_, name_file = min(koef_list)
file_name = os.path.basename(name_file)
print(file_name)