"""
Ćwiczenie nr 25

Znajdowanie wielokrotności liczby np dla wartości 3 do 12 zwrócisz [3, 6, 9, 12]
Wprowadzenie:
Twoim zadaniem jest napisanie funkcji, która przyjmuje dwie wartości: liczbę całkowitą (integer) oraz limit. Funkcja powinna zwrócić listę wielokrotności tej liczby aż do wartości limit włącznie. Jeśli limit jest wielokrotnością liczby, powinien być również uwzględniony w wynikowym zestawieniu. Do funkcji będą przekazywane wyłącznie dodatnie liczby całkowite, z wyjątkiem 0. Limit zawsze będzie większy niż podstawowa liczba.

Punkty do wykonania:
1. Funkcja powinna przyjmować dwie liczby całkowite jako argumenty: liczbę oraz limit.
2. Funkcja powinna zwracać listę wielokrotności liczby aż do wartości limit włącznie.
3. Wszystkie wartości w zwracanej liście powinny być dodatnimi liczbami całkowitymi.
Podpowiedź:
Rozważ użycie pętli i operatora modulo (%) do sprawdzenia, czy dana liczba jest wielokrotnością podanej liczby."""

# Opcja 1

"""
def findMultiples(integer, limit):
    return [i for i in range(integer, limit+1, integer)]
"""

# Opcja 2


def findMultiples(number, limit):
    result = []
    for i in range(number, limit + 1):
        if i % number == 0:
            result.append(i)
    return result


print(findMultiples(5, 25))
