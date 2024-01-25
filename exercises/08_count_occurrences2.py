"""Ćwiczenie nr 8
Zliczanie powtórzeń liczb w liście
Wprowadzenie:
Twoim zadaniem jest napisanie funkcji, która zliczy, ile razy dana liczba pojawia się w przekazanej liście. Funkcja powinna zwrócić słownik (w Pythonie nazywany "dictionary"), w którym kluczem jest liczba, a wartością - ilość jej powtórzeń w liście.
Punkty:
1. Utwórz funkcję o nazwie countOccurrences.
2. Funkcja powinna przyjmować jeden argument: numbersList.
3. Użyj pętli i słownika, aby zliczyć powtórzenia każdej liczby w liście.
4. Zwróć słownik z liczbami i ich ilościami powtórzeń.
5. Upewnij się, że funkcja działa poprawnie dla różnych wartości.
Podpowiedź:
Aby zliczyć powtórzenia liczb w liście, możesz użyć pętli, która przechodzi przez każdy element listy i zwiększa wartość w słowniku dla danego klucza (liczby)."""


def countOccurrences(numbersList):
    occurrencesDict = {}
    for number in numbersList:
        if number in occurrencesDict:
            occurrencesDict[number] += 1
        else:
            occurrencesDict[number] = 1
    return occurrencesDict


lista1 = [1, 2, 3, 1, 2, 1, 3, 4, 1, 6]
print(countOccurrences(lista1))
