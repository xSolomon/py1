import os

def directory_content(path : str, file_extension : str, include_one_sublevel : bool) -> list:
    directories : list[str] = []
    files : list[str] = []
    if os.path.isdir(path):
        for file_or_dir in os.listdir(path):
            path_to_subdir : str = os.path.join(path, file_or_dir)
            if os.path.isdir(path_to_subdir):
                if include_one_sublevel:
                    subdirectory_content : list = directory_content(path_to_subdir, \
						file_extension, False)
                    files.extend(subdirectory_content[0])
                    directories.extend(subdirectory_content[1])
                    directories.append(file_or_dir)
            elif file_or_dir.endswith(file_extension):
                files.append(file_or_dir)
    return [files, directories]