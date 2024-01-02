"""
Ćwiczenie z kodowania - continue
Wprowadzenie:
Celem tego zadania jest iteracja przez listę liczb całkowitych od 1 do 10 i wydrukowanie każdej liczby, chyba że jest ona wielokrotnością 3. W przypadku wielokrotności 3, pętla powinna kontynuować do następnej iteracji bez drukowania liczby, używając instrukcji continue.
Kroki do wykonania:
1. Utwórz pętlę for, która będzie iterować przez liczby od 1 do 10 włącznie.
2. W ciele pętli sprawdź, czy bieżąca liczba jest wielokrotnością 3.
3. Jeśli tak, użyj instrukcji continue do przejścia do następnej iteracji pętli.
4. W przeciwnym razie wydrukuj bieżącą liczbę.
Podpowiedź:
Aby sprawdzić, czy liczba jest wielokrotnością innej liczby, możesz użyć operatora reszty z dzielenia %.
"""

for v in range(1, 11):
    if v % 3 != 0:
        print(v)
        continue
