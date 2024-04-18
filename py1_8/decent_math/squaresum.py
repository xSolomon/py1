'''
	Модуль, содержащий функцию квадрата суммы
'''

#from simple_math.square import square as sq
#from simple_math.cube import cube as cu
import simple_math as sm

def square_sum(a : int, b : int) -> int:
	''' Формула квадрата суммы '''
	return sm.square.square(a) + 2 * a * b + sm.square.square(b)