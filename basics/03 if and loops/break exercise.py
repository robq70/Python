"""
Ćwiczenie z kodowania - break
Wprowadzenie:
Celem tego zadania jest iteracja przez listę liczb całkowitych od 1 do 10 i wydrukowanie pierwszej liczby, która jest podzielna przez 5. Gdy taka liczba zostanie znaleziona, pętla powinna zostać przerwana za pomocą instrukcji break.
Kroki do wykonania:
1. Utwórz pętlę for, która będzie iterować przez liczby od 1 do 10 włącznie.
2. W ciele pętli sprawdź, czy bieżąca liczba jest podzielna przez 5.
3. Jeśli tak, wydrukuj tę liczbę i natychmiast przerwij pętlę za pomocą instrukcji break.
Podpowiedź:
Aby sprawdzić, czy liczba jest podzielna przez inną liczbę, możesz użyć operatora reszty z dzielenia %.
"""
# Wpisz ponizej rozwiązanie

for v in range(1, 11):
    if v % 5 == 0:
        print(v)
        break
