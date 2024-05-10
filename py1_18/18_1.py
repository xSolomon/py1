from random import randint, choices
import string

pairs_number : int = 100
initial_key : int = randint(-100, 100)
key_list : list = []
for i in range(pairs_number):
    key_list.append(initial_key + i)

random_string_length : int = 10
int_str_dict : dict = dict()

for i in range(pairs_number):
    int_str_dict[key_list[i]] = ''.join(choices(string.ascii_letters, k = random_string_length))
    
for i in range(pairs_number):
    print(int_str_dict.get(key_list[i]))
    
for i in range(pairs_number):
    int_str_dict.pop(key_list[i])
    
print(int_str_dict)