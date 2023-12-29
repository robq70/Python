"""
Zadanie z sprawdzeniem długości łańcuchów znaków
1. Napisz funkcję compareStringLen która przyjmie dwa parametry str1 i str2
2. Funkcja sprawdza oba łańcuchy znaków, jeśli str1 jest dłuższy od str2 to funkcja zwróci true, w przeciwnym wypadku funkcja zwraca false
Podpowiedź:
Pamiętaj że w Python masz dostęp do funkcji len() która zwraca ilość znaków w łańcuchu
"""

def compareStringLen(str1, str2):
    """
    Funkcja porównuje długość dwóch łańcuchów znaków.

    Parametry:
    - str1 (str): Pierwszy łańcuch znaków.
    - str2 (str): Drugi łańcuch znaków.

    Zwraca:
    - bool: True jeśli str1 jest dłuższy od str2, w przeciwnym wypadku False.
    """

    # Używamy funkcji len() do porównania długości obu łańcuchów znaków.
    # Jeśli długość str1 jest większa od długości str2, zwracamy True.
    # W przeciwnym wypadku zwracamy False.
    # Napisz poniżej rozwiązanie zadania

    str1 = len(str1)
    str2 = len(str2)
    if str1 > str2:
        return True
    else:
        return False


example1 = "rthghghgfdfgdhgfdfdghfdg"
example2 = "fhggfhg"
define = compareStringLen(example1, example2)
print(define)
