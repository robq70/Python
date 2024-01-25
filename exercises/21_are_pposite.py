"""
Ćwiczenie nr 21
Sprawdź, czy dwa łańcuchy znaków są przeciwnościami czyli zachodzi taka sytuacja dla dwóch poniższych łańcuchów:

abcd
dcba

Wprowadzenie:
Masz do dyspozycji dwie zmienne typu string: s1 i s2. Twoim zadaniem jest napisanie funkcji, która sprawdzi, czy te dwa łańcuchy są przeciwnościami. Jeśli tak, funkcja powinna zwrócić wartość True, w przeciwnym razie False.
Punkty do wykonania:
1. Utwórz funkcję o nazwie areOpposite.
2. Funkcja powinna przyjmować dwa argumenty: s1 i s2.
3. Jeśli łańcuchy są przeciwnościami (jeden jest odwróconym drugiego), funkcja powinna zwrócić True.
4. W przeciwnym przypadku funkcja powinna zwrócić False.

Podpowiedź:
Upewnij się, że oba łańcuchy mają tę samą długość przed sprawdzeniem, czy są przeciwnościami."""


def areOpposite(s1, s2):
    if len(s1) != len(s2):
        return False
    if s1 == s2[::-1]:
        return True


a1 = "abcd"
a2 = "dcba"
print(areOpposite(a1, a2))
