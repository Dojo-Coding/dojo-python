

from tkinter import N
from typing import List, Optional

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers_sorteds: List[int] = sorted(numbers)
    n: Optional[int] = None
    lista: List[int] = []

    for number in numbers_sorteds:
        if number != n:
            n = number
            lista.append(n)
        
    return lista



        
def remove_duplicates_fn(numbers: List[int]) -> List[int]:
    def _apply(numbers: List[int] = [], state: Optional[int] = None, index: int = 0) -> List[int]:
        if len(numbers) == 0:
                return []
            
        if numbers[index] == state:
            numbers.remove(numbers[index])
        
        return _apply(numbers=numbers, state=numbers[index], index=index + 1)

    numbers_sorted = sorted(numbers)
    return _apply(numbers=numbers_sorted)

# [1, 2, 3], s=1
#
#

# state =
# index