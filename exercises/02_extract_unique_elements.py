"""
Ćwiczenie nr 2
Ekstrakcja unikalnych elementów z listy
Wprowadzenie:
Podczas analizy danych często spotykamy się z koniecznością usunięcia duplikatów. Twoim zadaniem jest napisanie funkcji, która przyjmuje listę jako argument i zwraca nową listę zawierającą tylko unikalne elementy z przekazanej listy.
Punkty do wykonania:
1. Utwórz funkcję o nazwie extractUniqueElements, która przyjmuje jeden argument - listę o nazwie inputList.
2. Funkcja powinna zwracać nową listę zawierającą tylko unikalne elementy z przekazanej listy.
3. Nie korzystaj z gotowych funkcji lub metod do usuwania duplikatów. Rozwiąż to zadanie samodzielnie.
Podpowiedź:
Możesz użyć pętli for do iteracji przez każdy element listy i sprawdzenia, czy dany element już istnieje w nowej liście. Jeśli nie, dodaj go do nowej listy.
"""


def extractUniqueElements(inputlist):
    lista = []
    for i in inputlist:
        if i not in lista:
            lista.append(i)
    return lista


trrr = [1, 2, 3, 5, 7, 4, 3, 2, 1]

print(extractUniqueElements(trrr))
