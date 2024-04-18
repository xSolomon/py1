'''
    Массив из 500 случайных объектов Car
    Добавлен метод print() к иерархии Car
'''

''' Данная программа наглядно демонстрирует полиморфизм подтипов.
    Благодаря ему мы можем пользоваться единым интерфейсом для разных типов иерархии.
    Интерпретатор автоматически выбирает нужную версию метода print(), в зависимости
    от типа параметра: print(FreightCar freight_car) или print(PassengerCar passenger_car)
'''

from random import randint
from copy import deepcopy
from functools import reduce
from collections import deque

def consume_entirely(iterator):
    ''' Полностью поглощает итератор, в частности, результат использования map '''
    deque(iterator, maxlen = 0)

class Car:
    ''' Абстрактный вагон '''
    def __init__(self, speed : int):
        self._speed = speed # Начальная скорость вагона, км/ч
        if self._speed < 0:
            self._speed = 0
    
    def set_speed(self, speed : int) -> None:
        ''' Движение вагона с заданной скоростью '''
        self._speed = speed
        if self._speed < 0:
            self._speed = 0
    
    def stop(self) -> None:
        ''' Остановка вагон '''
        self._speed = 0
        
    def print(self) -> None:
        print('Car::print()')
    
class FreightCar(Car):
    ''' Грузовой вагон, способный вместить лишь один тип товара '''
    def __init__(self, speed : int, cargo : str, cargo_weight : int):
        super().__init__(speed)
        self._cargo = cargo # Название перевозимого товара
        self._cargo_weight = cargo_weight # Масса груза, тонн
        if self._cargo_weight < 0:
            self._cargo_weight = 0
    
    def get_cargo_weight(self) -> int:
        ''' Возвращает массу груза '''
        return self._cargo_weight
    
    def get_cargo_name(self) -> str:
        ''' Возвращает наименование товара '''
        return self._cargo
    
    def _change_cargo_weight(self, cargo_weight) -> None:
        ''' Изменение массы груза текущего типа в вагоне '''
        self._cargo_weight += cargo_weight
        if self._cargo_weight < 0:
            self._cargo_weight = 0
    
    def _change_cargo(self, cargo, cargo_weight) -> None:
        ''' Замена текущего груза в вагоне на другой '''
        self._cargo = cargo
        self._change_cargo_weight(cargo_weight)
    
    def unload(self) -> None:
        ''' Выгрузка товар из вагона '''
        self._change_cargo('', 0)
    
    def load(cargo : str, cargo_weight : int) -> None:
        ''' Добавление товара того же типа или замена груза на новый '''
        if cargo == self._cargo:
            self._change_cargo_weight(cargo_weight)
        else:
            self.unload()
            self._change_cargo(cargo, cargo_weight)
    
    def print(self) -> None:
        print('FreightCar::print()')
    
class PassengerCar(Car):
    ''' Пассажирский вагон '''
    def __init__(self, speed : int, passengers_number : int,
        conductor_id : int):
        super().__init__(speed)
        self._conductor_id = conductor_id # Идентификатор проводника, закреплённого за вагоном
        self._passengers_number = passengers_number # Количество пассажиров в вагоне
        if self._passengers_number < 0:
            self._passengers_number = 0
    
    def get_passengers_number(self) -> int:
        ''' Возвращает число пассажиров в вагоне '''
        return self._passengers_number
    
    def add_passengers(self, passengers_number_delta : int) -> None:
        ''' Изменяет количество пассажиров в вагоне на указанное число.
            Положительное означает посадку, отрицательное - высадку '''
        self._passengers_number += passengers_number_delta
        if self._passengers_number < 0:
            self._passengers_number = 0
    
    def unload() -> None:
        ''' Высадка всех находящихся в поезде пассажиров '''
        self.passengers_number = 0
    
    def change_conductor(self, conductor_id : int) -> None:
        ''' Закрепление другого проводника за вагоном '''
        self._conductor_id = conductor_id
        
    def print(self) -> None:
        print('PassengerCar::print()')

def get_random_car() -> Car:
    ''' Возвращает объект случайного типа из двух: PassengerCar и FreightCar '''
    return FreightCar(0, '', 0) if randint(0, 1) else PassengerCar(0, 0, 0)

car_list : list = [get_random_car() for i in range(500)]
consume_entirely(map(lambda car : car.print(), car_list))
print(len(car_list))

