"""
Sprawdzenie parzystości liczby w Python ćwiczenie z kodowania

Wymagania:

    Napisz funkcję o nazwie is_even, która przyjmie jeden parametr o nazwie number.

    Funkcja powinna zwrócić True, jeśli liczba jest parzysta, w przeciwnym razie powinna zwrócić False.


Podpowiedź:

Liczba parzysta to taka liczba, która dzieli się przez 2 bez reszty. Możesz to sprawdzić za pomocą operatora modulo %.
"""
def is_even(number):
    """
    Funkcja sprawdza, czy podana liczba jest liczbą parzystą.

    Parametry:
    - number (int): Liczba do sprawdzenia.

    Zwraca:
    - bool: True jeśli liczba jest parzysta, w przeciwnym wypadku False.
    """
    
    # Używamy operatora % (reszta z dzielenia) do sprawdzenia, czy liczba dzieli się przez 2 bez reszty.
    # Jeśli tak, zwracamy True, w przeciwnym wypadku zwracamy False.
    if number%2 == 0:
        print("Liczba jest parzysta")
        return True
    else:
        print("Liczba jest nieparzysta")
        return False
    
n=is_even(10)