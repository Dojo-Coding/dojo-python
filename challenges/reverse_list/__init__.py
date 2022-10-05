from typing import List

def reverse_list(lista: List[int]) -> List[int]:
  lista_auxiliar: List[int] = []
  lenght: int = len(lista)

  # for index in range(lenght - 1, -1, -1):
  #   lista_auxiliar.append(lista[index])

  for index in range(lenght):
    lista_auxiliar.insert(0, lista[index])

  return [lista[index]for index in range(lenght - 1, -1, -1)]