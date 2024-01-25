"""Ćwiczenie nr 23

Połączenie dwóch łańcuchów znaków w formacie krótki+długi+krótki.
Wprowadzenie:
Masz do dyspozycji dwie zmienne tekstowe, a i b. Twoim zadaniem jest napisanie funkcji, która zwróci jeden łańcuch znaków w formacie krótki+długi+krótki, gdzie krótszy łańcuch znaków znajduje się na zewnątrz, a dłuższy w środku. Łańcuchy znaków nie będą miały tej samej długości, ale mogą być puste.
Punkty do wykonania:
1. Utwórz funkcję o nazwie combineStrings.
2. Funkcja powinna przyjmować dwa argumenty - łańcuchy znaków a i b.
3. Funkcja powinna zwrócić jeden łańcuch znaków w formacie krótki+długi+krótki.

Podpowiedź:
Sprawdź długość obu łańcuchów znaków i w zależności od tego, który jest dłuższy, zwróć odpowiednią kombinację."""


def combineStrings(a, b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b


aa = "a"
bb = "abc"
print(combineStrings(aa, bb))
