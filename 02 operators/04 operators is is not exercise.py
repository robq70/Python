"""
Użycie operatorów is i is not w Pythonie
Wprowadzenie:
W Pythonie operatory is i is not są używane do porównywania tożsamości obiektów, a nie ich wartości. Są one często używane w przypadku porównywania z wartościami None, ale mogą być używane do porównywania tożsamości dowolnych obiektów.
Kroki do wykonania:
1. Utwórz dwie zmienne listA i listB, które obie mają wartość [1, 2, 3].
2. Utwórz trzecią zmienną listC, która jest przypisana do tej samej referencji co listA (tzn. listC = listA).
3. Sprawdź, czy listA i listB są tym samym obiektem za pomocą operatora is i zapisz wynik w zmiennej isSameObjectAandB.
4. Sprawdź, czy listA i listC są tym samym obiektem za pomocą operatora is i zapisz wynik w zmiennej isSameObjectAandC.
5. Sprawdź, czy listA nie jest tym samym obiektem co listB za pomocą operatora is not i zapisz wynik w zmiennej isNotSameObjectAandB.
Podpowiedź:
Pamiętaj, że is porównuje tożsamość obiektów, a nie ich wartości. Dwa różne obiekty mogą mieć tę samą wartość, ale nie będą tym samym obiektem.
"""
listA = [1, 2, 3]
listB = [1, 2, 3]
listC = listA
isSameObjectAandB = listA is listB
isSameObjectAandC = listA is listC
isNotSameObjectAandB = listA is not listB
