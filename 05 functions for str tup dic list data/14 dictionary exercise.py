"""
Ćwiczenie z słownikiem
Wprowadzenie:
W tym zadaniu Twoim celem będzie napisanie funkcji, która zwróci wartość dla podanego klucza ze słownika. Jeśli klucz nie istnieje w słowniku, funkcja powinna zwrócić wartość domyślną.
Kroki do wykonania:
1. Zdefiniuj funkcję o nazwie get_value_from_dict, która przyjmie dwa parametry: dictionary (słownik, z którego chcemy uzyskać wartość) i key (klucz, dla którego chcemy uzyskać wartość).
2. Funkcja powinna zwrócić wartość dla podanego klucza ze słownika.
3. Jeśli klucz nie istnieje w słowniku, funkcja powinna zwrócić napis "Key not found".
Podpowiedź:
W Pythonie możesz użyć metody get() dla słowników, aby uzyskać wartość dla klucza i jednocześnie określić wartość domyślną, jeśli klucz nie istnieje.
"""


def get_value_from_dict(dictionary, key):
    """
    Funkcja zwraca wartość dla podanego klucza ze słownika lub wartość domyślną, jeśli klucz nie istnieje.

    Parametry:
    - dictionary (dict): Słownik, z którego chcemy uzyskać wartość.
    - key: Klucz, dla którego chcemy uzyskać wartość.

    Zwraca:
    - Wartość dla klucza lub napis "Key not found", jeśli klucz nie istnieje w słowniku.
    """
    if dictionary:
        return dictionary.get(key, "Key not found")
