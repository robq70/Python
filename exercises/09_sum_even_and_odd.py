"""Ćwiczenie nr 9
Suma liczb parzystych i nieparzystych w liście
Wprowadzenie:
Twoim zadaniem jest napisanie funkcji, która obliczy sumę liczb parzystych i nieparzystych w przekazanej liście. Funkcja powinna zwrócić krotkę, w której pierwszy element to suma liczb parzystych, a drugi element to suma liczb nieparzystych.
Punkty:
1. Utwórz funkcję o nazwie sumEvenAndOdd.
2. Funkcja powinna przyjmować jeden argument: numbersList.
3. Użyj pętli, aby obliczyć sumę liczb parzystych i nieparzystych w liście.
4. Zwróć krotkę z sumą liczb parzystych i nieparzystych.
5. Upewnij się, że funkcja działa poprawnie dla różnych wartości.
Podpowiedź:
Aby sprawdzić, czy liczba jest parzysta, możesz użyć operatora reszty z dzielenia (%). Jeśli number % 2 == 0, liczba jest parzysta."""


def sumEvenAndOdd(numbersList):
    sumEven = 0
    sumOdd = 0

    for number in numbersList:
        if number % 2 == 0:
            sumEven += number
        else:
            sumOdd += number
    return (sumEven, sumOdd)


liczby = (3, 7, 8, 12, 4, 6)
print(sumEvenAndOdd(liczby))
