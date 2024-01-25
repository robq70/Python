"""Ćwiczenie nr 10
Dodawanie liczb z łańcuchów znaków
Wprowadzenie:
Masz do napisania funkcję, która przyjmie dwa łańcuchy znaków reprezentujące liczby. Twoim zadaniem jest przekształcenie tych łańcuchów na liczby, a następnie zwrócenie ich sumy.
Punkty:
1. Utwórz funkcję o nazwie addStringsAsNumbers.
2. Funkcja powinna przyjmować dwa argumenty: stringNumber1 i stringNumber2.
3. Przekształć oba łańcuchy znaków na liczby.
4. Zwróć sumę obu liczb.
5. Upewnij się, że funkcja działa poprawnie dla różnych wartości.
Podpowiedź:
Możesz użyć funkcji int(), aby przekształcić łańcuch znaków na liczbę."""


def addStringsAsNumbers(stringNumber1, stringNumber2):
    strToInt1 = int(stringNumber1)
    strToInt2 = int(stringNumber2)
    sumInt = strToInt1 + strToInt2
    return sumInt


print(addStringsAsNumbers(9, 7))
