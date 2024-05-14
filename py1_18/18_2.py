from random import randint
from collections import defaultdict

def frequent_values(val_list : list[int], minimum_times_occured : int) -> list[int]:
    ''' Возвращает список значений, встречающихся не меньше заданного количества раз '''
    list_len : int = 100
    assert len(val_list) == list_len
    vals_frequency : defaultdict[int, int] = defaultdict(lambda : 0)
    result : list[int] = []
    for val in val_list:
        vals_frequency[val] += 1
        if vals_frequency[val] == minimum_times_occured:
            result.append(val)
    assert len(result) <= len(vals_frequency)
    return result
    
v_list : list[int] = list(map(lambda x : randint(1, 10), range(100)))

print(frequent_values(v_list, 10))
