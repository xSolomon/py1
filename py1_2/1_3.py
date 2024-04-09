'''
    Демонстрация побочных эффектов передачи по ссылке
'''

class Unit:
    name : str = 'Крестьянин' # Название боевой единицы
    attack : int = 1 # Атака
    defence : int = 1 # Защита
    health : int = 1 # Максимальное здоровье
    speed : int = 3 # Скорость передвижения
    min_damage : int = 1 # Минимальный урон
    max_damage : int = 1 # Максимальный урон
    
def print_unit(unit : Unit) -> None:
    print(f'Название: {unit.name}')
    print(f'Атака: {unit.attack}')
    print(f'Защита: {unit.defence}')
    print(f'Здоровье: {unit.health}')
    print(f'Скорость: {unit.speed}')
    print(f'Минимальный урон: {unit.min_damage}')
    print(f'Максимальный урон: {unit.max_damage}')
    
def print_class(class_instance : Unit) -> None:
    if isinstance(class_instance, Unit):
        print_unit(class_instance)
    else:
        print('Неизвестный класс')

def change_unit(unit : Unit) -> None:
    ''' Изменяет имя юнита на "Кочевник" '''
    if isinstance(unit, Unit):
        unit.name = 'Кочевник'
    else:
        print('Ошибка, неверный тип аргумента') 
        
unit_angel = Unit()
unit_angel.name = 'Ангел'
unit_angel.attack = 20
unit_angel.defence = 20
unit_angel.health = 200
unit_angel.speed = 12
unit_angel.min_damage = 50
unit_angel.max_damage = 50

print_unit(unit_angel)
unit_nomad = unit_angel
change_unit(unit_nomad) # Передача по ссылке, обе переменные ссылаются на один объект
print_unit(unit_angel) # Неожиданные изменения в имени юнита

