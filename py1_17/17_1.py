''' Урок 17, задание 1 '''
import os
from PIL import Image
from directory import directory_content

def change_images_extenstion(from_ext : str, to_ext : str) -> None:
    ''' Изменяет формат всех изображений указанного расширения в текущем каталоге '''
    for im in directory_content('.', from_ext, False)[0]:
        try:
            image : Image = Image.open(im)
            if to_ext == '.jpg' and image.mode in ('RGBA', 'P'):
                image = image.convert('RGB')
            image.save(os.path.splitext(im)[0] + to_ext)
        except:
            print(f'Ошибка при попытке изменения расширения изображения {im}')
                