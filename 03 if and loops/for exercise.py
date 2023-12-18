"""
Pętla for - ćwiczenie z kodowania
Wprowadzenie:
Mnożenie liczb z listy to często spotykane zadanie w programowaniu. W tym zadaniu skupimy się na mnożeniu tylko nieparzystych liczb z określonego zakresu.
Kroki do wykonania:
1. Utwórz listę numbers zawierającą liczby od -4 do 4 (włącznie) z krokiem co 1.
2. Zdefiniuj zmienną result o wartości początkowej 1. Będzie to zmienna przechowująca wynik mnożenia.
3. Użyj pętli for do iteracji po liście numbers.
4. W ciele pętli sprawdź, czy aktualna liczba jest nieparzysta.
5. Jeśli liczba jest nieparzysta, pomnóż wartość zmiennej result przez tę liczbę.
6. Po zakończeniu pętli wydrukuj wartość zmiennej result.
Podpowiedź:
Aby sprawdzić, czy liczba jest nieparzysta, możesz użyć operatora reszty z dzielenia (%). Jeśli number % 2 jest różne od zera, oznacza to, że liczba jest nieparzysta.
"""
numbers = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
result = 1
for n in numbers:
    if n % 2 != 0:
        result *= n
print(result)
