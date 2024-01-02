"""
Ćwicznenie z kodowania z zagnieżdżonymi pętlami
Wprowadzenie:
Celem tego zadania jest wydrukowanie tabliczki mnożenia dla liczb od 1 do 3 za pomocą zagnieżdżonych pętli for.
Kroki do wykonania:
1. Użyj zewnętrznej pętli for do iteracji po liczbach od 1 do 3 włącznie.
2. Wewnątrz tej pętli użyj wewnętrznej pętli for do iteracji również po liczbach od 1 do 3 włącznie.
3. W ciele wewnętrznej pętli drukuj wynik mnożenia obu liczb, a następnie przejdź do nowej linii.
Rezultatem w konsoli działania programu będzie:
    1
    2
    3
    2
    4
    6
    3
    6
    9
"""

for n in range(1, 4):
    for v in range(1, 4):
        s = n * v
        print(s)
