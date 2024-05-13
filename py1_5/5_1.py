'''
    Две косвенно связанные иерархии классов:
    Вагон: грузовой/пассажирский
    Поезд: грузовой/пассажирский
'''

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
        ''' Остановка вагона '''
        self._speed = 0
    
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
    
    def change_passengers(self, passengers_number_delta : int) -> None:
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

class DieselLocomotive():
    ''' Тепловоз, работающий на дизельном топливе '''
    def __init__(self, speed : int, fuel : int):
        self._speed : int = speed # Начальная скорость локомотива, км/ч
        self._fuel : int = fuel # Объём топлива, л
    
    def move(self, speed : int, cars_number : int = 0) -> bool:
        ''' Движение локомотива с заданной скоростью. Расходует топливо, пропорциональное 
            количеству вагонов, которые движутся в составе.
            Топливо расходует и сам локомотив'''
        if speed <= 0:
            self._speed = 0
            return True
        if cars_number < 0:
            cars_number = 0
        fuel_cost = (cars_number + 1) * 15
        if self._fuel >= fuel_cost:
            self._fuel -= fuel_cost
            self._speed = speed
            return True
        return False
            
    
    def stop(self) -> None:
        ''' Остановка локомотива '''
        self._speed = 0
    
    def change_fuel(self, fuel_delta : int) -> None:
        ''' Изменение количества топлива в баках на указанное число.
            Положительное означает пополнение, отрицательное - слив топлива из баков.'''
        self._fuel == fuel_delta
        if self._fuel < 0:
            self._fuel = 0
        
   
class Train():
    def __init__(self, speed : int, locomotive : DieselLocomotive):
        self._speed = speed # Начальная скорость, км/ч
        if self._speed < 0:
            self._speed = 0
        self._locomotive : DieselLocomotive = locomotive # Локомотив поезда, обязателен
        self._car_list : list = [] # Список вагонов поезда
    
    def cars_number(self) -> int:
        ''' Возвращает число вагонов в данном поезде '''
        return len(self._car_list)
     
    def move(self, speed : int) -> bool:
        ''' Движение поезда с заданной скоростью. Возвращает True в случае, если у 
            локомотива достаточно топлива для движения, иначе False.'''
        if speed < 0:
            speed = 0
        if self._locomotive.move(speed, len(self._car_list)):
            consume_entirely(map(lambda car : car.set_speed(self._speed), self._car_list))
            return True
        return False

    def stop(self) -> None:
        ''' Остановка поезда '''
        self._speed = 0
        self._locomotive.stop()
        consume_entirely(map(lambda car : car.stop(), self._car_list))
    
    def change_fuel(self, fuel_delta : int) -> None:
        ''' Изменение количества топлива в баках на указанное число.
            Положительное означает пополнение, отрицательное - слив топлива из баков.'''
        self.stop()
        self._locomotive.change_fuel(fuel_delta)
    
    def add_car(self, car : Car) -> None:
        ''' Добавляет вагон к составу. Осуществляется глубокое копирование '''
        self._car_list.append(deepcopy(car))
        self._car_list[-1].set_speed(self._speed)
    
    def remove_car(self, car_index : int) -> Car:
        ''' Удаляет вагон под заданным номером из состава и возвращает ссылку на него '''
        return self._car_list.pop(car_index)
        
class FreightTrain(Train):
    def __init__(self, speed : int, locomotive : DieselLocomotive, freight_car_list : list = []):
        super().__init__(speed, locomotive)
        consume_entirely(map(self.add_car, freight_car_list))
    
    def add_car(self, freight_car : FreightCar) -> bool:
        ''' Добавляет грузовой вагон к составу. Возвращает True в случае успеха и False иначе '''
        if isinstance(freight_car, FreightCar):
            super().add_car(freight_car)
            return True
        else:
            return False
    
    def add_cargo(self, car_index : int, cargo : str, cargo_weight : int) -> None:
        ''' Добавление груза в указанный вагон.
            Возвращает True в случае успеха и False иначе ''' 
        self.stop()
        self._car_list[car_index].load(cargo, cargo_weight)
    
    def unload(self) -> None:
        ''' Остановка и опустошение всех вагонов '''
        self.stop()
        consume_entirely(map(lambda freight_car : freight_car.unload(), self._car_list))
    
class PassengerTrain(Train):
    def __init__(self, speed : int, locomotive : DieselLocomotive, passenger_car_list : list = []):
        super().__init__(speed, locomotive)
        consume_entirely(map(self.add_car, passenger_car_list))
    
    def add_car(self, passenger_car : PassengerCar) -> bool:
        ''' Добавляет пассажирский вагон к составу. Возвращает True в случае успеха и False иначе. '''
        if isinstance(passenger_car, PassengerCar):
            super().add_car(passenger_car)
            return True
        else:
            return False
    
    def change_passengers(self, car_index : int, passengers_number_delta : int) -> None:
        ''' Изменяет количество пассажиров в указанном вагоне.
            Положительное число означает посадку, отрицательное - высадку '''
        self.stop()
        self._car_list[car_index].change_passengers(passengers_number_delta)
    
    def unload(self) -> None:
        ''' Остановка и высадка всех пассажиров из поезда '''
        self.stop()
        consume_entirely(map(lambda passenger_car : passenger_car.unload(), self._car_list))
    
        
locomotive1 = DieselLocomotive(0, 1000)
freight_car1 = FreightCar(0, "Уголь", 100)
freight_car2 = FreightCar(0, "Железная руда", 200)

freight_train1 = FreightTrain(0, locomotive1, [freight_car1, freight_car2])
freight_train1.unload()
print(freight_train1.move(10))
print(freight_train1.cars_number())

locomotive2 = DieselLocomotive(0, 0)
passenger_car1 = PassengerCar(100, 37, 1)
passenger_car2 = PassengerCar(0, 46, 2)
print(passenger_car1.get_passengers_number())

passenger_train1 = PassengerTrain(50, locomotive2)
print(passenger_train1.move(17))
passenger_train1.add_car(passenger_car1)
passenger_train1.add_car(passenger_car2)
passenger_train1.change_fuel(100)
print(passenger_train1.move(17))
passenger_train1.change_passengers(1, -46)
passenger_car3 = passenger_train1.remove_car(-1)
print(passenger_car3.get_passengers_number())




