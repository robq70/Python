"""Ćwiczenie nr 26

Dodawanie długości słowa do samego siebie
Wprowadzenie:
Twoim zadaniem jest napisanie funkcji, która przyjmuje łańcuch znaków składający się z kilku słów oddzielonych spacją. Funkcja powinna zwrócić listę, w której każde słowo jest połączone z jego długością. Np:
"Hello my friend" --> ["Hello 5", "my 2", "friend 6"]

Punkty do wykonania:
1. Funkcja powinna przyjmować łańcuch znaków jako argument.
2. Funkcja powinna zwracać listę słów z ich długościami.
3. Każde słowo w wynikowej liście powinno być połączone ze swoją długością za pomocą spacji.

Podpowiedź:
Rozważ użycie metody split() do podziału łańcucha znaków na listę słów. Następnie dla każdego słowa oblicz jego długość i połącz z nim."""


def lenghtOfWord(string):
    return [word + " " + str(len(word)) for word in string.split()]


string1 = "Hello my friend"
print(lenghtOfWord(string1))
