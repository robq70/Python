"""Ćwiczenie nr 16

Konwersja słów na ich długość.
Wprowadzenie:
Masz daną listę słów. Twoim zadaniem jest napisanie funkcji, która przekształci każde słowo na jego długość.
Punkty:
1. Utwórz funkcję o nazwie convertWordsToLength.
2. Funkcja powinna przyjmować jeden argument: wordsList (lista słów).
3. Funkcja powinna zwrócić nową listę, w której każde słowo zostało zastąpione jego długością.
4. Jeśli lista jest pusta, funkcja powinna zwrócić pustą listę.
Podpowiedź:
Użyj pętli lub składni list comprehension, aby przeiterować przez każde słowo w liście i zastąpić je jego długością."""


def convertWordsToLength(wordsList):
    return [len(word) for word in wordsList]


lista1 = ["Olaf", "Ala"]
print(convertWordsToLength(lista1))
