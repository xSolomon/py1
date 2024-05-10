import os
import shutil

def delete_directory(path : str) -> bool:
    if not os.path.isdir(path):
        return False
    for file_or_dir in os.listdir(path):
        if os.path.isdir(os.path.join(path, file_or_dir)):
            return False
    shutil.rmtree(path)
    return True
