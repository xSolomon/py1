from random import randint
from collections import defaultdict

def frequent_values(val_list : list, minimum_times_occured : int) -> list:
    ''' Возвращает список значений, встречающихся не меньше заданного количества раз '''
    list_len : int = 100
    assert len(val_list) == list_len
    vals_frequency : defaultdict = defaultdict(lambda : 0)
    for val in val_list:
        vals_frequency[val] += 1
    result : list = []
    for key, value in vals_frequency.items():
        if value >= minimum_times_occured:
            result.append(key)
    assert len(result) <= list_len
    return result
    
v_list : list = list(map(lambda x : randint(1, 10), range(100)))

print(frequent_values(v_list, 10))