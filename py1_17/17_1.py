from PIL import Image
import os

def change_images_extenstion(from_ext : str, to_ext : str) -> None:
    ''' Изменяет формат всех изображений указанного расширения в текущем каталоге '''
    for file_or_dir in os.listdir():
        if os.path.isfile(file_or_dir) and file_or_dir.endswith(from_ext):
            try:
                image : Image = Image.open(file_or_dir)
                if to_ext == '.jpg' and image.mode in ('RGBA', 'P'):
                    image = image.convert('RGB')
                image.save(os.path.splitext(file_or_dir)[0] + to_ext)
            except:
                print(f'Ошибка при попытке изменения расширения изображения {file_or_dir}')