from zipfile import ZipFile

# with ZipFile("workbook.zip") as zip_file:
#     files_size = sum((zip_file.getinfo(info).file_size) for info in zip_file.namelist())
#     compress_size = sum((zip_file.getinfo(info).compress_size) for info in zip_file.namelist())

with ZipFile("workbook.zip") as zip_file:
    files_size = 0
    compress_size = 0

    for info in zip_file.infolist():
        if not info.is_dir():
            files_size += info.file_size
            compress_size += info.compress_size

print(f'Объем исходных файлов: {files_size} байт(а) ')
print(f'Объем сжатых файлов: {compress_size} байт(а) ')