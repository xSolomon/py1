'''
	Модуль, содержащий формулу куба суммы
'''

import simple_math as sm

def cube_sum(a : int, b : int) -> int:
	''' Формула куба суммы '''
	return sm.cube.cube(a) + 3 * sm.square.square(a) * b + 3 * a * sm.square.square(b) + sm.cube.cube(b)