import random
from typing import List
def get_unique_list_numbers() -> List[int]:
    n=0
    spisok =[]
    while n != 15:
        random_int = random.randint(-10, 10) # TODO написать функцию для получения списка уникальных целых чисел
        if not random_int in spisok:
            spisok.append(random_int)
            n+=1
    return spisok
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))