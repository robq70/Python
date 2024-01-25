"""Ćwiczenie nr 20

Koszt reklamy na billboardzie.
Wprowadzenie:
Wyobraź sobie, że chcesz umieścić swoje imię i nazwisko na wielkim billboardzie reklamowym. Każdy znak ma stałą cenę 50$. Twoim zadaniem jest obliczenie całkowitego kosztu napisu, który chcesz umieścić na billboardzie.
Punkty:
1. Utwórz funkcję o nazwie billboardCost.
2. Funkcja powinna przyjmować jeden argument: text (łańcuch znaków).
3. Funkcja powinna zwrócić całkowity koszt napisu na billboardzie.
4. Pamiętaj, że spacja również jest liczbą i ma koszt 50$.
Podpowiedź:
Rozważ użycie pętli do iteracji przez każdy znak w łańcuchu i sumowanie kosztu każdego znaku."""

# Opcja 1
"""
def billboardCost(text):
    costPerCharacter = 50
    totalCost = 0
    for char in text:
        totalCost += costPerCharacter
    return totalCost
"""
# Opcja 2


def billboardCost(tekst):
    koszt = len(tekst)
    return koszt * 50


tekst1 = "Nasz partia jest najlepsza"
print(billboardCost(tekst1))
