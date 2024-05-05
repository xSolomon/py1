'''
    Создаёт 10 файлов с именами 1.txt, 2.txt, ..., 10.txt и пишет в них 3 числа, 
    каждое с новой строки
'''

from random import randint

for i in range(1, 11):
    with open(f'files/{i}.txt', "wt") as fout:
        for i in range(3):
            fout.write(f"{randint(-100, 100)}\n")
