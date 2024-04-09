'''
    ���������� ������ ������, ���������� � ����� �� ���� HoMM3
'''

class Unit:
    name : str = '����������' # �������� ������ �������
    attack : int = 1 # �����
    defence : int = 1 # ������
    health : int = 1 # ������������ ��������
    speed : int = 3 # �������� ������������
    min_damage : int = 1 # ����������� ����
    max_damage : int = 1 # ������������ ����
    
magic_schools : tuple = ['����', '�����', '�����', '������']

class Spell:
    name : str = '���������' # �������� ����������
    manacost : int = 6 # ��������� ����
    magic_schools : set = ['������'] # ����� �����, � ������� ����������� ����������

class Hero:
    name : str = '�����' # ��� �����
    attack : int = 1 # �����
    defence : int = 0 # ������
    spell_power : int = 2 # ���� ����������
    knowledge : int = 2 # ������
    skills : dict = { # ������ � ������� �������� (�������, ����������� ��� ����������)
        '��������': '�������',
        '����������': '�������'
    }
    
def print_unit(unit : Unit) -> None:
    print(f'��������: {unit.name}')
    print(f'�����: {unit.attack}')
    print(f'������: {unit.defence}')
    print(f'��������: {unit.health}')
    print(f'��������: {unit.speed}')
    print(f'����������� ����: {unit.min_damage}')
    print(f'������������ ����: {unit.max_damage}')

def print_spell(spell : Spell) -> None:
    print(f'��������: {spell.name}')
    print(f'��������: {spell.manacost}')
    print('����� �����, � ������� ��������� ����������:')
    for magic_school in spell.magic_schools:
        print(f'    {magic_school}')

def print_hero(hero : Hero) -> None:
    print(f'���: {hero.name}')
    print(f'�����: {hero.attack}')
    print(f'������: {hero.defence}')
    print(f'���� ����������: {hero.spell_power}')
    print(f'������: {hero.knowledge}')
    print('������:')
    for skill, level in hero.skills.items():
        print(f'    {skill}: {level}')
    
def print_class(class_instance : Unit | Spell | Hero) -> None:
    if isinstance(class_instance, Unit):
        print_unit(class_instance)
    elif isinstance(class_instance, Spell):
        print_spell(class_instance)
    elif isinstance(class_instance, Hero):
        print_hero(class_instance)
    else:
        print('����������� �����')

unit_angel = Unit()
unit_angel.name = '�����'
unit_angel.attack = 20
unit_angel.defence = 20
unit_angel.health = 200
unit_angel.speed = 12
unit_angel.min_damage = 50
unit_angel.max_damage = 50
print_class(unit_angel)

spell_magic_arrow = Spell()
spell_magic_arrow.name = '��������� ������'
spell_magic_arrow.manacost = 5
spell_magic_arrow.magic_schools = magic_schools
print_class(spell_magic_arrow)

hero_valeska = Hero()
hero_valeska.name = "�������"
hero_valeska.attack = 2
hero_valeska.defence = 2
hero_valeska.spell_power = 0
hero_valeska.knowledge = 1
hero_valeska.skills = {
    '���������': '�������',
    '��������': '�������'
}
print_class(hero_valeska)

