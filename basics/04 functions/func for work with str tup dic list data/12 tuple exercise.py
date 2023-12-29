"""
Ćwiczenie z krotką
Wprowadzenie:
W tym zadaniu Twoim celem będzie napisanie funkcji, która zwróci krotkę składającą się z największej i najmniejszej liczby z podanej listy liczb.
Kroki do wykonania:
1. Zdefiniuj funkcję o nazwie min_and_max, która przyjmie jeden parametr o nazwie numbers.
2. Funkcja powinna zwrócić krotkę składającą się z najmniejszej i największej liczby z listy numbers.
3. Jeśli lista jest pusta, funkcja powinna zwrócić pustą krotkę.
Podpowiedź:
W Pythonie masz dostęp do funkcji min() i max(), które zwracają odpowiednio najmniejszą i największą wartość z listy.
"""


def min_and_max(numbers):
    """
    Funkcja zwraca krotkę składającą się z najmniejszej i największej liczby z podanej listy.

    Parametry:
    - numbers (list): Lista liczb.

    Zwraca:
    - tuple: Krotka składająca się z najmniejszej i największej liczby z listy lub pusta krotka, jeśli lista jest pusta.
    """

    # Napisz rozwiązanie
    if numbers:
        return min(numbers), max(numbers)
    return ()


lista = (3, 4, 5, 6)
print(min_and_max(lista))
