'''
    Список объектов на основе данных из файла
'''

class Hero:
    def __init__(self, name : str, level : int, move_points : int, units_in_army : int,
        attack : int, defence : int, spell_power : int, knowledge : int):
        self.__name : str = name # Имя героя
        self.__level : int = level # Уровень героя
        self.__move_points: int = move_points # Запас хода
        self.__units_in_army : int = units_in_army # Количество существ в армии героя
        self.__attack : int = attack # Атака
        self.__defence : int = defence # Защита
        self.__spell_power : int = spell_power # Сила заклинаний
        self.__knowledge : int = knowledge # Знания
        assert self.__level >= 0 and self.__move_points >= 0 and self.__units_in_army >= 0 \
            and self.__attack >= 0 and self.__defence >= 0 and self.__spell_power >= 0 and self.__knowledge >= 0
            
    def load_hero_from_string(data_string : str):
        ''' Загружает героя из строки '''
        data : list[str] = data_string.rstrip().split(' ')
        return Hero(data[0], int(data[1]), int(data[2]), int(data[3]),
            int(data[4]), int(data[5]), int(data[6]), int(data[7]))
        


hero_list : list[Hero] = []
try:
    with open('input.txt') as fin:
        for line in fin:
            try:
                hero = Hero.load_hero_from_string(line)
                hero_list.append(hero)
            except:
                print(f'Строка {line} содержит неверную информацию')
         
except:
    print('Непредвиденная ошибка')