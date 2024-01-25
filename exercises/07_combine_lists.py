"""Ćwiczenie nr 7
Połączenie dwóch list w jedną
Wprowadzenie:
Twoim zadaniem jest napisanie funkcji, która połączy dwie listy w jedną. Funkcja powinna przyjmować dwie listy jako argumenty i zwracać jedną listę, która jest połączeniem obu list. Nie możesz używać żadnych wbudowanych funkcji do łączenia list.
Punkty:
1. Utwórz funkcję o nazwie combineLists.
2. Funkcja powinna przyjmować dwa argumenty: list1 i list2.
3. Użyj pętli, aby dodać elementy z obu list do nowej listy.
4. Zwróć połączoną listę.
5. Upewnij się, że funkcja działa poprawnie dla różnych wartości.
Podpowiedź:
Aby połączyć dwie listy, możesz najpierw utworzyć pustą listę, a następnie dodać do niej elementy z obu list za pomocą pętli."""


def combineLists(list1, list2):
    combineLists = []
    for i in list1:
        combineLists.append(i)
    for i in list2:
        combineLists.append(i)
    return combineLists


lista1 = [2, 3]
lista2 = [4, 5]

print(combineLists(lista1, lista2))
