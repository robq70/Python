"""Ćwiczenie nr 14

Podnoszenie parzystych liczb do kwadratu.
Wprowadzenie:
Masz daną listę liczb. Twoim zadaniem jest napisanie funkcji, która podniesie do kwadratu wszystkie parzyste liczby z tej listy.
Punkty:
1. Utwórz funkcję o nazwie squareEvenNumbers.
2. Funkcja powinna przyjmować jeden argument: numbers (lista liczb).
3. Dla każdej parzystej liczby w liście numbers, podnieś ją do kwadratu.
4. Zwróć listę z liczbami po modyfikacji.
Podpowiedź:
Możesz użyć pętli for do iteracji przez listę i warunku if do sprawdzenia, czy liczba jest parzysta."""


def squareEvenNumbers(numbers):
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            numbers[i] = numbers[i] ** 2
    return numbers


list1 = [4, 12, 22]
print(squareEvenNumbers(list1))
