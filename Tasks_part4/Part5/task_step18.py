import os.path
from zipfile import ZipFile


result_files = []
with ZipFile("workbook.zip") as zip_file:
    for info in zip_file.infolist():
        if not info.is_dir():
            file_name = os.path.basename(info.filename)
            date_time = info.date_time
            formatted_date = f"{date_time[0]}-{date_time[1]}-{date_time[2]} {date_time[3]}:{date_time[4]}:{date_time[5]}"
            result_files.append(
                (file_name,
                 formatted_date,
                 info.file_size,
                 info.compress_size
                 ))

result_files.sort(key=lambda x: [0])
for i, (name, form_date, file_size, compress_size) in enumerate(result_files):
    print(f"{name}\n"
          f"    Дата модификации файла: {form_date}\n"
          f"    Объем исходного файла: {file_size} байт(а)\n"
          f"    Объем сжатого файла: {compress_size} байт(а)")

    if i < len(result_files) - 1:
        print()


