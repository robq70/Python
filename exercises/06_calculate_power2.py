"""Ćwiczenie nr 6
Obliczanie potęgi liczby
Wprowadzenie:
Twoim zadaniem jest napisanie funkcji, która oblicza potęgę danej liczby. Funkcja powinna przyjmować dwie liczby: bazę i wykładnik, a następnie zwracać wynik bazy podniesionej do potęgi wykładnika. Nie możesz używać żadnych wbudowanych funkcji do obliczania potęgi.
Punkty:
1. Utwórz funkcję o nazwie calculatePower.
2. Funkcja powinna przyjmować dwa argumenty: base i exponent.
3. Użyj pętli, aby obliczyć potęgę liczby.
4. Zwróć wynik.
5. Upewnij się, że funkcja działa poprawnie dla różnych wartości.
Podpowiedź:
Aby obliczyć potęgę liczby, pomnóż bazę przez siebie tyle razy, ile wynosi wykładnik. Pamiętaj, że każda liczba podniesiona do potęgi 0 wynosi 1."""


def calculatePower(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result


print(calculatePower(3, 4))
