"""
Ćwiczenie nr 22

Konwersja elementów tablicy na jeden łańcuch znaków z przecinkami.
Wprowadzenie:
Masz do dyspozycji tablicę elementów. Twoim zadaniem jest napisanie funkcji, która przekształci wszystkie elementy tej tablicy w jeden łańcuch znaków, w którym elementy są oddzielone przecinkami.
Punkty do wykonania:
1. Utwórz funkcję o nazwie convertArrayToString.
2. Funkcja powinna przyjmować jeden argument - tablicę elementów.
3. Funkcja powinna zwrócić jeden łańcuch znaków, w którym elementy są oddzielone przecinkami.
Podpowiedź:
Możesz użyć metody join dla łańcuchów znaków, aby połączyć elementy tablicy w jeden łańcuch."""


def convertArrayToString(elements):
    return ",".join(map(str, elements))


table1 = ["Ala", "ma", "kota"]
print(convertArrayToString(table1))
