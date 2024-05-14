''' Урок 17, задание 1 '''
import os
from PIL import Image
from directory import directory_content

def change_images_extenstion(from_ext : str, to_ext : str) -> bool:
    ''' Изменяет формат всех изображений указанного расширения в текущем каталоге '''
    success : bool = True
    image_list : list[str] = directory_content('.', from_ext, False)[0]
    for im in image_list:
        try:
            image : Image = Image.open(im)
            if to_ext == '.jpg' and image.mode in ('RGBA', 'P'):
                image = image.convert('RGB')
            image.save(os.path.splitext(im)[0] + to_ext)
        except:
            success = False
    return success
                