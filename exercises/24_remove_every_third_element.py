"""
Ćwiczenie nr 24

Usuwanie co trzeciego elementu z listy

Wprowadzenie:
Masz daną listę elementów. Twoim zadaniem jest napisanie funkcji, która usunie z tej listy co trzeciego elementu, zaczynając od trzeciego elementu. Pierwsze dwa elementy zawsze powinny pozostać na swoim miejscu.

Punkty do wykonania:

    Funkcja powinna przyjmować jedną listę jako argument.

    Funkcja powinna zwracać nową listę, w której usunięto co trzeciego elementu, zaczynając od trzeciego.

    Pierwsze dwa elementy powinny zawsze pozostać na swoim miejscu.

Podpowiedź:
Rozważ użycie pętli i indeksowania listy do rozwiązania tego zadania.
"""


def removeEveryThirdElement(lst):
    result = []
    for i in range(len(lst)):
        if (i + 1) % 3 != 0 or i < 2:
            result.append(lst[i])
    return result


lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(removeEveryThirdElement(lista1))
