'''
    Упрощенная модель юнитов, заклинаний и героя из игры HoMM3
'''

class Unit:
    name : str = 'Крестьянин' # Название боевой единицы
    attack : int = 1 # Атака
    defence : int = 1 # Защита
    health : int = 1 # Максимальное здоровье
    speed : int = 3 # Скорость передвижения
    min_damage : int = 1 # Минимальный урон
    max_damage : int = 1 # Максимальный урон
    
magic_schools : tuple = ['Вода', 'Огонь', 'Земля', 'Воздух']

class Spell:
    name : str = 'Ускорение' # Название заклинания
    manacost : int = 6 # Стоимость маны
    magic_schools : set = ['Воздух'] # Школы магии, к которым принадлежит заклинание

class Hero:
    name : str = 'Адель' # Имя героя
    attack : int = 1 # Атака
    defence : int = 0 # Защита
    spell_power : int = 2 # Сила заклинаний
    knowledge : int = 2 # Знания
    skills : dict = { # Навыки и уровень владения (Базовый, Продвинутый или Экспертный)
        'Мудрость': 'Базовый',
        'Дипломатия': 'Базовый'
    }
    
def print_unit(unit : Unit) -> None:
    print(f'Название: {unit.name}')
    print(f'Атака: {unit.attack}')
    print(f'Защита: {unit.defence}')
    print(f'Здоровье: {unit.health}')
    print(f'Скорость: {unit.speed}')
    print(f'Минимальный урон: {unit.min_damage}')
    print(f'Максимальный урон: {unit.max_damage}')

def print_spell(spell : Spell) -> None:
    print(f'Название: {spell.name}')
    print(f'Манакост: {spell.manacost}')
    print('Школы магии, к которым относится заклинание:')
    for magic_school in spell.magic_schools:
        print(f'    {magic_school}')

def print_hero(hero : Hero) -> None:
    print(f'Имя: {hero.name}')
    print(f'Атака: {hero.attack}')
    print(f'Защита: {hero.defence}')
    print(f'Сила заклинаний: {hero.spell_power}')
    print(f'Знания: {hero.knowledge}')
    print('Навыки:')
    for skill, level in hero.skills.items():
        print(f'    {skill}: {level}')
    
def print_class(class_instance : Unit | Spell | Hero) -> None:
	''' Вывод информации об объектах на экран '''
	if isinstance(class_instance, Unit):
	    print_unit(class_instance)
	elif isinstance(class_instance, Spell):
	    print_spell(class_instance)
	elif isinstance(class_instance, Hero):
	    print_hero(class_instance)
	else:
	    print('Неизвестный класс')

unit_angel = Unit()
unit_angel.name = 'Ангел'
unit_angel.attack = 20
unit_angel.defence = 20
unit_angel.health = 200
unit_angel.speed = 12
unit_angel.min_damage = 50
unit_angel.max_damage = 50
print_class(unit_angel)

spell_magic_arrow = Spell()
spell_magic_arrow.name = 'Волшебная стрела'
spell_magic_arrow.manacost = 5
spell_magic_arrow.magic_schools = magic_schools
print_class(spell_magic_arrow)

hero_valeska = Hero()
hero_valeska.name = "Валеска"
hero_valeska.attack = 2
hero_valeska.defence = 2
hero_valeska.spell_power = 0
hero_valeska.knowledge = 1
hero_valeska.skills = {
    'Лидерство': 'Базовый',
    'Стрельба': 'Базовый'
}
print_class(hero_valeska)



