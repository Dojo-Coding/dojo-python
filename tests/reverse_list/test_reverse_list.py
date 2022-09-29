
from challages.reverse_list import reverse_list


def test_reverse_list():
    lista_invertida = reverse_list([1, 2, 3])
    assert lista_invertida == [3, 2, 1]