"""
Ćwiczenie z scope
Kroki do wykonania:
1. Utwórz globalną zmienną o nazwie globalVar i przypisz jej wartość 10.
2. Napisz funkcję o nazwie modifyVariables, która:
    Utworzy lokalną zmienną o nazwie localVar i przypisze jej wartość 5.
    Zmodyfikuje wartość globalVar, dodając do niej wartość localVar.
    Wydrukuje wartość globalVar wewnątrz funkcji.
3. Wywołaj funkcję modifyVariables.
4. Wydrukuj wartość globalVar poza funkcją.

Podpowiedź:
Aby odwołać się do globalnej zmiennej wewnątrz funkcji, użyj słowa kluczowego global przed nazwą zmiennej. Na przykład: global globalVar.
"""

globalVar = 10


def modifyVariables():
    localVar = 5
    global globalVar
    globalVar = globalVar + localVar
    print(f"Wewnątrz funkcji: {globalVar}")


modifyVariables()
print(f"Poza funkcją: {globalVar}")
