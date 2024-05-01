'''
    Упрощенная модель юнитов, заклинаний и героя из игры HoMM3
    Все поля сделаны приватными, добавлены некоторые проверки на допустимые границы значений
    Для тренировки некоторым полям добавлены сеттеры и геттеры
'''

from random import randint

class Unit:
    def __init__(self, name : str, attack : int, defence : int, health : int,
        speed : int, min_damage : int, max_damage : int):
        self.__name : str = name # Название боевой единицы
        self.__attack : int = attack # Атака
        self.__defence : int = defence # Защита
        self.__health : int = health # Максимальное здоровье
        self.__speed : int = speed # Скорость передвижения
        self.__min_damage : int = min_damage # Минимальный урон
        self.__max_damage : int = max_damage # Максимальный урон
        
    def print(self) -> None:
        ''' Вывод информации о юните '''
        print(f'Название: {self.__name}')
        print(f'Атака: {self.__attack}')
        print(f'Защита: {self.__defence}')
        print(f'Здоровье: {self.__health}')
        print(f'Скорость: {self.__speed}')
        print(f'Минимальный урон: {self.__min_damage}')
        print(f'Максимальный урон: {self.__max_damage}')

class Castle:
    def __init__(self, name : str, money : int, income : int, unit_income : int,
        available_units : int, units_in_harrizon : int):
        self.__name : str = name # Имя замка
        self.__money : int = money # Количество денег в казне замка
        self.__income : int = income # Прирост денег за день
        self.__unit_income : int = unit_income # Прирост существ в замке за неделю
        self.__available_units : int = available_units # Количество существ, доступных для найма
        self.__units_in_harrizon : int = units_in_harrizon # Количество существ в гарнизоне замка
        
    def get_units_in_harrizon(self) -> int:
        return self.__units_in_harrizon
    
    def set_units_in_harrizon(self, value) -> None:
        self.__units_in_harrizon = 0 if value <= 0 else value
    
    def upgrade_income(self) -> None:
        ''' Увеличивает ежедневный доход замка, затрачивая деньги '''
        if self.__money >= 5000:
            self.__money -= 5000
            self.__income += 2000
        
    def upgrade_unit_income(self) -> None:
        ''' За плату увеличивает еженедельный прирост существ '''
        if self.__money >= 1500:
            self.__money -= 1500
            self.__unit_income += 25
        
    def buy_units(self) -> None:
        ''' Купить часть доступных для найма существ и поместить их в гарнизон '''
        if self.__money >= 3000 and self.__available_units >= 20:
            self.__money -= 3000
            self.__available_units -= 20
            self.__units_in_harrizon += 20
        
    def refill(self) -> None:
        ''' Каждую неделю число доступных для найма существ и денег увеличивается
            на соответствующий им прирост '''
        self.__available_units += self.__unit_income
        self.__money += self.__income
        
    def print(self) -> None:
        ''' Вывод информации о замке '''
        print(f'Имя: {self.__name}')
        print(f'Денег в казне: {self.__money}')
        print(f'Доход: {self.__income}')
        print(f'Прирост существ: {self.__unit_income}')
        print(f'Доступно существ для найма: {self.__available_units}')
        print(f'Существ в гарнизоне: {self.__units_in_harrizon}')
        
class Hero:
    def __init__(self, name : str, level : int, move_points : int, units_in_army : int,
        is_in_castle : bool, attack : int, defence : int, spell_power : int, knowledge : int):
        self.__name : str = name # Имя героя
        self.__level : int = level # Уровень героя
        self.__move_points: int = move_points # Запас хода
        self.__units_in_army : int = units_in_army # Количество существ в армии героя
        self.__is_in_castle : bool = is_in_castle # Находится ли герой в данный момент в замке
        self.__attack : int = attack # Атака
        self.__defence : int = defence # Защита
        self.__spell_power : int = spell_power # Сила заклинаний
        self.__knowledge : int = knowledge # Знания
        
    def move(self) -> bool:
        ''' Герой двигается по карте '''
        if self.__move_points >= 500:
            self.__move_points -= 500
            self.__is_in_castle = False
            return True
        return False
    
    def return_to_castle(self) -> bool:
        ''' Герой возвращается в ближайший замок '''
        if self.__move_points >= 500:
            self.__move_points -= 500
            self.__is_in_castle = True
            return True
        return False
        
    def rest(self) -> None:
        ''' Герой отдыхает ночью, восстанавливая запас хода '''
        self.__move_points += 2000
        
    def level_up(self) -> bool:
        ''' Герой ищет на карте сражения, получая новый уровень и увеличивая атрибут '''
        if self.__move_points >= 1500 and self.__units_in_army >= 15:
            self.__move_points -= 1500
            self.__is_in_castle = False
            self.__units_in_army -= 15
            self.__level += 1
            match randint(1, 4):
                case 1:
                    self.__attack += 1
                case 2:
                    self.__defence += 1
                case 3:
                    self.__spell_power += 1
                case 4:
                    self.__knowledge += 1
            return True
        return False
                    
    def take_army_from_castle_harrizon(self, army : int, castle :  Castle) -> bool:
        ''' Герой забирает армию из гарнизона любого из городов, при условии его
            нахождения в каком-нибудь из замков и наличии достаточного количества существ '''
        if self.__is_in_castle and army >= 0 and castle.get_units_in_harrizon() >= army:
            self.__units_in_army += army
            castle.set_units_in_harrizon(castle.get_units_in_harrizon() - army)
            return True
        return False
        
    def refill_army(self, castle : Castle) -> bool:
        ''' Герой возвращается в замок и пополняет армию '''
        if self.return_to_castle() and self.take_army_from_castle_harrizon(50, castle):
            return True
        return False
        
    def print(self) -> None:
        ''' Вывод информации о герое '''
        print(f'Имя: {self.__name}')
        print(f'Уровень: {self.__level}')
        print(f'Запас хода: {self.__move_points}')
        print(f'Существ в армии: {self.__units_in_army}')
        print(f'Атака: {self.__attack}')
        print(f'Защита: {self.__defence}')
        print(f'Сила заклинаний: {self.__spell_power}')
        print(f'Знания: {self.__knowledge}')

castle1 = Castle('Бреттония', 15000, 2500, 20, 60, 10)
castle2 = Castle('Александретта', 10000, 2000, 10, 40, 0)
hero1 = Hero('Адель', 1, 2000, 50, 1, True, 0, 2, 2)
hero2 = Hero('Валеска', 1, 1000, 100, False, 2, 2, 0, 1)

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




