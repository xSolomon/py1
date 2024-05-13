'''
    Чтение данных из файла и обработка ошибок
'''

from random import randint

def sum_six_numbers_from_two_random_files(first_number : int = randint(1, 10),
    second_number : int = randint(1, 10), filepath : str = 'files/') -> list[int, int]:
    ''' Возвращает сумму шести чисел из двух файлов с именами, заданными аргументами 
        функции и расширением .txt
        Возвращает пару значений: итоговая сумма и код ошибки, где код ошибки:
        0 - ошибок нет
        1 - один из файлов не существует
        2 - один из файлов содержит неполные или повреждённые данные
        3 - иные ошибки'''
    filename_list : list = [f'{filepath}{i}.txt' for i in [first_number, second_number]]
    number_sum : int = 0
    error_code : int = 0
    try:
        for filename in filename_list:
            with open(filename) as fin:
                for i in range(3):
                    number_sum += int(fin.readline().rstrip())
    except FileNotFoundError:
        number_sum = 0
        error_code = 1
    except ValueError:
        number_sum = 0
        error_code = 2
    except:
        number_sum = 0
        error_code = 3
    return [number_sum, error_code]

print(sum_six_numbers_from_two_random_files()[1])