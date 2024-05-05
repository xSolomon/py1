'''
    Чтение данных из файла и обработка ошибок
'''

from random import randint

def sum_six_numbers_from_two_random_files(first_number : int = randint(1, 10),
    second_number : int = randint(1, 10), filepath : str = 'files/') -> int | str:
    ''' Возвращает сумму шести чисел из двух файлов с именами, заданными аргументами 
        функции и расширением .txt
        В случае ошибки возвращает строку-сообщение с подробностями'''
    filename_list : list[str] = [f'{filepath}{i}.txt' for i in [first_number, second_number]]
    number_sum : int = 0
    for filename in filename_list:
        try:
            with open(filename) as fin:
                for i in range(3):
                    number_sum += int(fin.readline().rstrip())
        except FileNotFoundError:
            return f'Ошибка. Файл с именем {filename} не существует'
        except ValueError:
            return f'Ошибка. Файл с именем {filename} содержит неполные или повреждённые данные'
    return number_sum
	
print(sum_six_numbers_from_two_random_files())