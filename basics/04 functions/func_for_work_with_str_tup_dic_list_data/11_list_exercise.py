"""
Ćwiczenie z listą
1. Zdefiniuj funkcję o nazwie get_first_element, która przyjmie jeden parametr o nazwie lst.
2. Funkcja powinna zwrócić pierwszy element z listy lst.
3. Jeśli lista jest pusta, funkcja powinna zwrócić None.
"""


def get_first_element(lst):
    """
    Funkcja zwraca pierwszy element z podanej listy.

    Parametry:
    - lst (list): Lista, z której chcemy uzyskać pierwszy element.

    Zwraca:
    - Pierwszy element z listy lub None, jeśli lista jest pusta.
    """

    if lst:
        return lst[0]
    return None


regis = get_first_element([])
print(regis)
