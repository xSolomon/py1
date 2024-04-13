'''
    Упрощенная модель юнитов, заклинаний и героя из игры HoMM3
    Класс Spell заменён классом Castle
    Изменены свойства класса Hero
    Также добавлены конструкторы у всех классов и методы у классов Castle и Hero
'''

from random import randint

class Unit:
    def __init__(self, name : str, attack : int, defence : int, health : int,
        speed : int, min_damage : int, max_damage : int):
        self.name : str = name # Название боевой единицы
        self.attack : int = attack # Атака
        self.defence : int = defence # Защита
        self.health : int = health # Максимальное здоровье
        self.speed : int = speed # Скорость передвижения
        self.min_damage : int = min_damage # Минимальный урон
        self.max_damage : int = max_damage # Максимальный урон
    def print(self) -> None:
        ''' Вывод информации о юните '''
        print(f'Название: {self.name}')
        print(f'Атака: {self.attack}')
        print(f'Защита: {self.defence}')
        print(f'Здоровье: {self.health}')
        print(f'Скорость: {self.speed}')
        print(f'Минимальный урон: {self.min_damage}')
        print(f'Максимальный урон: {self.max_damage}')

class Castle:
    def __init__(self, name : str, money : int, income : int, unit_income : int,
        available_units : int, units_in_harrizon : int):
        self.name : str = name # Имя замка
        self.money : int = money # Количество денег в казне замка
        self.income : int = income # Прирост денег за день
        self.unit_income : int = unit_income # Прирост существ в замке за неделю
        self.available_units : int = available_units # Количество существ, доступных для найма
        self.units_in_harrizon : int = units_in_harrizon # Количество существ в гарнизоне замка
    def upgrade_income(self) -> None:
        ''' Увеличивает ежедневный доход замка, затрачивая деньги '''
        self.money -= 5000
        self.income += 2000
    def upgrade_unit_income(self) -> None:
        ''' За плату увеличивает еженедельный прирост существ '''
        self.money -= 1500
        self.unit_income += 25
    def buy_units(self) -> None:
        ''' Купить часть доступных для найма существ и поместить их в гарнизон '''
        self.money -= 3000
        self.available_units -= 20
        self.units_in_harrizon += 20
    def refill(self) -> None:
        ''' Каждую неделю число доступных для найма существ и денег увеличивается
            на соответствующий им прирост '''
        self.available_units += self.unit_income
        self.money += self.income
    def print(self) -> None:
        ''' Вывод информации о замке '''
        print(f'Имя: {self.name}')
        print(f'Денег в казне: {self.money}')
        print(f'Доход: {self.income}')
        print(f'Прирост существ: {self.unit_income}')
        print(f'Доступно существ для найма: {self.available_units}')
        print(f'Существ в гарнизоне: {self.units_in_harrizon}')
class Hero:
    def __init__(self, name : str, level : int, move_points : int, units_in_army : int,
        attack : int, defence : int, spell_power : int, knowledge : int):
        self.name : str = name # Имя героя
        self.level : int = level # Уровень героя
        self.move_points: int = move_points # Запас хода
        self.units_in_army : int = units_in_army # Количество существ в армии героя
        self.attack : int = attack # Атака
        self.defence : int = defence # Защита
        self.spell_power : int = spell_power # Сила заклинаний
        self.knowledge : int = knowledge # Знания
    def move(self) -> None:
        ''' Герой двигается по карте '''
        self.move_points -= 500
    def rest(self) -> None:
        ''' Герой отдыхает ночью, восстанавливая запас хода '''
        self.move_points += 2000
    def level_up(self) -> None:
        ''' Герой ищет на карте сражения, получая новый уровень и увеличивая атрибут'''
        self.move_points -= 1500
        self.units_in_army -= 15
        self.level += 1
        match randint(1, 4):
            case 1:
                self.attack += 1
            case 2:
                self.defence += 1
            case 3:
                self.spell_power += 1
            case 4:
                self.knowledge += 1
    def refill_army(self, castle : Castle) -> None:
        ''' Герой возвращается в замок и пополняет армию '''
        self.move()
        castle.units_in_harrizon -= 50
        self.units_in_army += 50
    def print(self) -> None:
        ''' Вывод информации о герое '''
        print(f'Имя: {self.name}')
        print(f'Уровень: {self.level}')
        print(f'Запас хода: {self.move_points}')
        print(f'Существ в армии: {self.units_in_army}')
        print(f'Атака: {self.attack}')
        print(f'Защита: {self.defence}')
        print(f'Сила заклинаний: {self.spell_power}')
        print(f'Знания: {self.knowledge}')

castle1 = Castle('Бреттония', 15000, 2500, 20, 60, 10)
castle2 = Castle('Александретта', 10000, 2000, 10, 40, 0)
hero1 = Hero('Адель', 1, 2000, 50, 1, 0, 2, 2)
hero2 = Hero('Валеска', 1, 1000, 100, 2, 2, 0, 1)

castle1.upgrade_income()
castle1.upgrade_unit_income()
castle1.buy_units()
castle1.print()
print()

hero1.move()
hero1.level_up()
hero1.print()
print()

hero2.rest()
hero2.level_up()
hero2.level_up()
hero2.rest()
hero2.refill_army(castle1)
hero2.print()
print()

castle2.upgrade_unit_income()
castle2.refill()
castle2.buy_units()
castle2.buy_units()
castle2.buy_units()

hero2.refill_army(castle2)
castle2.print()
print()
hero2.print()




