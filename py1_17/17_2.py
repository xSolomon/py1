from PIL import Image, ImageDraw
import os
from directory import directory_content

def write_text_in_center_and_save_as(from_ext : str, to_ext : str) -> None:
    ''' Изменяет формат всех изображений указанного расширения в текущем каталоге.
        Также в центре каждого изображения рисует квадрат и пишет внутри этого квадрата текст'''
    for im in directory_content('.', from_ext, False)[0]:
        try:
            image : Image = Image.open(im)
            if to_ext == '.jpg' and image.mode in ('RGBA', 'P'):
                image = image.convert('RGB')
            canvas : ImageDraw = ImageDraw.Draw(image)
            size : tuple = image.size
            # Квадрат размером 50x50
            canvas.rectangle([size[0] / 2 - 25,size[1] / 2 - 25, \
                size[0] / 2 + 25,size[1] / 2 + 25])
            canvas.multiline_text((size[0] / 2 - 20, size[1] / 2 - 20), 'Hello,\nWorld!')
            image.save(os.path.splitext(im)[0] + to_ext)
            del canvas
        except:
            print(f'Ошибка при попытке изменения расширения изображения {im}')
