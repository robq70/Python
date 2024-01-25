"""
Ćwiczenie nr 4
Znajdź najdłuższe słowo w zdaniu
Wprowadzenie:
Analiza tekstu to często spotykane zadanie w programowaniu. W tym zadaniu Twoim celem jest napisanie funkcji, która znajdzie i zwróci najdłuższe słowo w podanym zdaniu.
Punkty do wykonania:
1. Utwórz funkcję o nazwie findLongestWord, która przyjmuje jeden argument - ciąg znaków o nazwie sentence.
2. Funkcja powinna zwracać najdłuższe słowo z przekazanego zdania.
3. Użytkownik musi użyć pętli do analizy zdania. Nie korzystaj z gotowych funkcji lub metod do dzielenia ciągów znaków.
Podpowiedź:
Możesz iterować przez każdy znak w zdaniu, zbierając słowa i porównując ich długość, aby znaleźć najdłuższe.
"""


def findLongestWord(sentence):
    words = sentence.split()
    # Ala ma kota poprzez split zwraca ["Ala","ma","kota"]
    longest_word = ""
    for word in words:
        word = word.replace(".", "")
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


zdanie1 = "Nie korzystaj z gotowych funkcjonalnosci."
print(findLongestWord(zdanie1))
