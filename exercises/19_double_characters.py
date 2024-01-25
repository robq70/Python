"""Ćwiczenie nr 19

Podwajanie znaków w łańcuchu znaków.
Wprowadzenie:
Często podczas przetwarzania tekstu możemy chcieć modyfikować łańcuchy znaków w różny sposób. Twoim zadaniem jest napisanie funkcji, która dla danego łańcucha znaków zwróci nowy łańcuch, w którym każdy znak (z uwzględnieniem wielkości liter) zostanie powtórzony raz.
Punkty:
1. Utwórz funkcję o nazwie doubleCharacters.
2. Funkcja powinna przyjmować jeden argument: text (łańcuch znaków).
3. Funkcja powinna zwrócić nowy łańcuch znaków, w którym każdy znak z oryginalnego łańcucha zostanie powtórzony raz.
4.Funkcja powinna uwzględniać wielkość liter.
Podpowiedź:
Rozważ użycie pętli do iteracji przez każdy znak w łańcuchu i dodawanie tego samego znaku do wynikowego łańcucha dwa razy."""


def doubleCharacters(text):
    result = ""
    for char in text:
        result += char * 2
    return result


string1 = "Ala ma kota a kot ma ale"
print(doubleCharacters(string1))
