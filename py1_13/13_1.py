'''
    Тестирование функции сортировки различными видами тестов
'''

import unittest
import pytest
from parametrize import parametrize
from random import randint

class BubbleSortTests(unittest.TestCase):
    ''' Набор тестов для функции сортировки '''
    def test_regression_1(self) -> None:
        ''' Регрессивный тест, массив из 10 чисел в обратном порядке '''
        test_list : list[int] = [i for i in range(10, 0, -1)]
        bubble_sort(test_list)
        self.assertEqual(test_list, [i for i in range(1, 11)])
        
    def test_regression_2(self) -> None:
        test_list : list[int] = [i for i in range(1, 10)]
        bubble_sort(test_list)
        self.assertEqual(test_list, [i for i in range(1, 10)])
        
    def test_empty_list(self) -> None:
        test_list : list[int] = []
        bubble_sort(test_list)
        self.assertEqual(test_list, [])
        
    def test_border_values(self) -> None:
        test_list : list[int] = [9223372036854775807, -9223372036854775808, 9223372036854775807]
        bubble_sort(test_list)
        self.assertEqual(test_list, [-9223372036854775808, 9223372036854775807, 9223372036854775807])

    @parametrize('repeat_times', range(100))
    def test_random(self, repeat_times) -> None:
        test_list : list[int] = [randint(-1000, 1000) for i in range(1000)]
        sorted_list : list[int] = sorted(test_list)
        bubble_sort(test_list)
        self.assertEqual(test_list, sorted_list)
        
def bubble_sort(int_array : list[int]) -> None:
    ''' Сортировка массива чисел методом пузырька '''
    swaps_occured : bool = True
    for i in range(len(int_array)):
        swaps_occured = False
        for j in range(len(int_array) - i - 1):
            if int_array[j] > int_array[j + 1]:
                int_array[j], int_array[j + 1] = int_array[j + 1], int_array[j]
                swaps_occured = True
        if not swaps_occured:
            break;

pytest.main(["-x", "13_1.py"])
