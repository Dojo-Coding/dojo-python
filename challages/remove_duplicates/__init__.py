

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

