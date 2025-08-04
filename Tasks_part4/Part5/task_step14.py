from zipfile import ZipFile

with ZipFile("workbook.zip") as zip_file:
    file_info = sum(not info.is_dir() for info in zip_file.infolist())
print(file_info)

