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
