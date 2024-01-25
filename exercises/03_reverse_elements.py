"""
Ćwiczenie nr 3
Odwróć elementy listy
Wprowadzenie:
Często podczas analizy danych lub manipulowania danymi potrzebujemy odwrócić kolejność elementów w liście. Twoim zadaniem jest napisanie funkcji, która przyjmuje listę jako argument i zwraca nową listę z odwróconą kolejnością elementów.
Punkty do wykonania:
1. Utwórz funkcję o nazwie reverseElements, która przyjmuje jeden argument - listę o nazwie inputList.
2. Funkcja powinna zwracać nową listę z odwróconą kolejnością elementów z przekazanej listy.
3. Użytkownik musi użyć pętli do odwrócenia kolejności elementów. Nie korzystaj z gotowych funkcji lub metod do odwracania listy.
Podpowiedź:
Możesz zainicjować pustą listę i użyć pętli for do iteracji przez każdy element przekazanej listy, dodając każdy element na początek nowej listy.

"""


def reverseElements(inputlist):
    lista = []
    for i in inputlist:
        lista.insert(0, i)
    return lista


# list.insert(i, x)
# Wstawia element na podaną pozycję. Pierwszy argument jest indeksem elementu, przed który wstawiamy, więc a.insert(0, x) wstawia na początek listy a a.insert(len(a), x) odpowiada a.append(x).


trrr = [4, 6, 7, 8]


print(reverseElements(trrr))
