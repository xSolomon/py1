'''
    ������������ �������� �������� �������� �� ������
'''

class Unit:
    name : str = '����������' # �������� ������ �������
    attack : int = 1 # �����
    defence : int = 1 # ������
    health : int = 1 # ������������ ��������
    speed : int = 3 # �������� ������������
    min_damage : int = 1 # ����������� ����
    max_damage : int = 1 # ������������ ����
    
def print_unit(unit : Unit) -> None:
    print(f'��������: {unit.name}')
    print(f'�����: {unit.attack}')
    print(f'������: {unit.defence}')
    print(f'��������: {unit.health}')
    print(f'��������: {unit.speed}')
    print(f'����������� ����: {unit.min_damage}')
    print(f'������������ ����: {unit.max_damage}')
    
def print_class(class_instance : Unit) -> None:
    if isinstance(class_instance, Unit):
        print_unit(class_instance)
    else:
        print('����������� �����')

def change_unit(unit : Unit) -> None:
    ''' �������� ��� ����� �� "��������" '''
    if isinstance(unit, Unit):
        unit.name = '��������'
    else:
        print('������, �������� ��� ���������') 
        
unit_angel = Unit()
unit_angel.name = '�����'
unit_angel.attack = 20
unit_angel.defence = 20
unit_angel.health = 200
unit_angel.speed = 12
unit_angel.min_damage = 50
unit_angel.max_damage = 50

print_unit(unit_angel)
unit_nomad = unit_angel
change_unit(unit_nomad) # �������� �� ������, ��� ���������� ��������� �� ���� ������
print_unit(unit_angel) # ����������� ��������� � ����� �����

