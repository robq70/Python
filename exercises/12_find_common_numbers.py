"""Ćwiczenie nr 12

Znajdź wspólne liczby z dwóch list bez używania dodatkowych funkcji.
Wprowadzenie:
Twoim zadaniem jest napisanie funkcji, która przyjmie dwie listy liczb jako argumenty i zwróci listę liczb, które występują w obu listach, nie korzystając z żadnych wbudowanych funkcji ani metod.
Punkty:
1. Utwórz funkcję o nazwie findCommonNumbers.
2. Funkcja powinna przyjmować dwa argumenty: listA i listB.
3. Zwróć listę liczb, które występują zarówno w listA, jak i w listB.
4. Upewnij się, że zwracana lista nie zawiera duplikatów.
5. Upewnij się, że funkcja działa poprawnie dla różnych wartości.
Podpowiedź:
Rozpocznij od stworzenia pustej listy wynikowej. Następnie, dla każdej liczby z pierwszej listy, sprawdź, czy występuje ona w drugiej liście i czy nie została już dodana do listy wynikowej. Jeśli oba warunki są spełnione, dodaj liczbę do listy wynikowej."""


# Wersja 1
"""    
def findCommonNumbers(listA, listB):
    commonNumbers = []
    for num in listA:
        if num in listB and num not in commonNumbers:
            commonNumbers.append(num)
    return commonNumbers
        """


# Wersja 2
def findCommonNumbers(listA, listB):
    lista = []
    for number in listA:
        if number in listB:
            if number in lista:
                continue
            lista.append(number)
    return lista


list1 = [1, 3, 4, 6, 7, 6, 6, 1]
list2 = [1, 2, 5, 6, 9]
print(findCommonNumbers(list1, list2))
