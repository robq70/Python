"""
Zadanie z łańcuchami znaków

Kroki do wykonania:

    Zdefiniuj funkcję o nazwie first_and_last_letter, która przyjmie jeden parametr o nazwie s.

    Funkcja powinna zwrócić krotkę składającą się z pierwszej i ostatniej litery łańcucha znaków s.

    Jeśli łańcuch znaków jest pusty, funkcja powinna zwrócić pustą krotkę.

Podpowiedź:

W Pythonie, aby uzyskać dostęp do pierwszego i ostatniego elementu łańcucha znaków, użyj indeksu 0 oraz -1, np. s[0] i s[-1]. Pamiętaj, aby sprawdzić, czy łańcuch znaków nie jest pusty przed próbą dostępu do jego elementów.
"""


def first_and_last_letter(s):
    """
    Funkcja zwraca krotkę składającą się z pierwszej i ostatniej litery podanego łańcucha znaków.

    Parametry:
    - s (str): Łańcuch znaków.

    Zwraca:
    - tuple: Krotka składająca się z pierwszej i ostatniej litery łańcucha znaków lub pusta krotka, jeśli łańcuch jest pusty.
    """

    # Napisz rozwiązanie
    if s:
        return (s[0], s[-1])
    else:
        return ()
