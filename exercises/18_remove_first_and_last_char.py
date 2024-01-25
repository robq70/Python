"""Ćwiczenie nr 18

Usuwanie pierwszego i ostatniego znaku z łańcucha znaków.
Wprowadzenie:
Często podczas przetwarzania tekstu potrzebujemy modyfikować łańcuchy znaków w określony sposób. Twoim zadaniem jest napisanie funkcji, która usunie pierwszy i ostatni znak z danego łańcucha znaków.
Punkty:
1. Utwórz funkcję o nazwie removeFirstAndLastChar.
2. Funkcja powinna przyjmować jeden argument: text (łańcuch znaków).
3. Funkcja powinna zwrócić łańcuch znaków po usunięciu pierwszego i ostatniego znaku.
4. Jeśli długość łańcucha znaków jest mniejsza niż 2, funkcja powinna zwrócić pusty łańcuch.
Podpowiedź:
Rozważ użycie indeksowania łańcucha znaków do usunięcia pierwszego i ostatniego znaku.
Usuwanie pierwszego i ostatniego """

"""
def removeFirstAndLastChar(text):
    if len(text) < 2:
        return ""
    return text[1:-1]

"""


def removeFirstAndLastChar(text):
    if len(text) < 2:
        return ""
    else:
        return text[1:-1]


drops = ["ddd", "ffff", "gggg"]
print(removeFirstAndLastChar(drops))
