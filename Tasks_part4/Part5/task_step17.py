import os
from datetime import datetime
from zipfile import ZipFile

target_time = datetime(2021, 11, 30, 14,22)
result_files = []

with ZipFile("workbook.zip") as zip_file:
    for info in zip_file.infolist():
        if not info.is_dir():
            file_date = datetime(*info.date_time)

            if target_time < file_date:
                result_files.append(os.path.basename(info.filename))

for name in sorted(result_files):
    print(name)
