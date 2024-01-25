"""Ćwiczenie nr 5

Oblicz średnią z listy liczb
Wprowadzenie:
Obliczanie średniej to podstawowa operacja matematyczna, którą często stosuje się w analizie danych. W tym zadaniu Twoim celem jest napisanie funkcji, która obliczy średnią wartość liczb z podanej listy.
Punkty do wykonania:
1. Utwórz funkcję o nazwie calculateAverage, która przyjmuje jeden argument - listę liczb o nazwie numbers.
2. Funkcja powinna zwracać średnią wartość liczb z przekazanej listy.
3. Użytkownik musi użyć pętli do obliczenia sumy liczb i następnie podzielić ją przez ich ilość, aby uzyskać średnią. Nie korzystaj z gotowych funkcji lub metod do obliczania sumy.

Podpowiedź:
Możesz iterować przez każdą liczbę w liście, sumując je, a następnie podzielić sumę przez ilość liczb w liście, aby uzyskać średnią."""


def calculateAverage(numbers):
    lista = []
    if not numbers:
        return 0
    sum = 0
    for i in numbers:
        sum = i + sum
    return sum / len(numbers)


numery = [2, 3, 9, 7, 5, 6]
print(calculateAverage(numery))
