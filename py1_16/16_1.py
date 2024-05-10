import os
from zipfile import ZipFile

def add_files_to_archive(archive_name : str, file_extension : str) -> bool:
    ''' Создаёт в текущем каталоге архив и добавляет туда все файлы текущего каталога с заданным расширением '''

    with ZipFile(archive_name, 'w') as zip_out:
        for file_or_dir in os.listdir():
            if os.path.isfile(file_or_dir) and \
                (file_extension == '.*' or file_or_dir.endswith(file_extension)) and \
                file_or_dir != archive_name:
                zip_out.write(file_or_dir)