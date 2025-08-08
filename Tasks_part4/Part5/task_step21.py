from zipfile import ZipFile


def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zip_file:
        if not args:
            zip_file.extractall()
        else:
            all_files = zip_file.namelist()
            for file in args:
                if file in all_files:
                    zip_file.extract(file)
                else:
                    for archived_files in all_files:
                        if archived_files.split('/')[-1] == file:
                            zip_file.extract(archived_files)



extract_this('workbook.zip', 'earth.jpg', 'exam.txt')