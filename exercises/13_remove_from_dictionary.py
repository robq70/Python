"""Ćwiczenie nr 13

Usuwanie elementu ze słownika.
Wprowadzenie:
Masz daną funkcję, która przyjmuje słownik oraz klucz. Twoim zadaniem jest usunięcie z tego słownika elementu o podanym kluczu.
Punkty:
1. Utwórz funkcję o nazwie removeFromDictionary.
2. Funkcja powinna przyjmować dwa argumenty: dictionary (słownik) i key (klucz).
3. Usuń z dictionary element o podanym kluczu key.
4. Jeśli klucz nie istnieje w słowniku, funkcja powinna zwrócić słownik bez zmian.
5. Zwróć zmodyfikowany słownik.
Podpowiedź:
Aby usunąć klucz ze słownika, możesz użyć instrukcji del, ale pamiętaj, aby najpierw sprawdzić, czy klucz istnieje w słowniku."""


# Wersja 1
"""
def removeFromDictionary(dictionary, key):
    if key in dictionary:
        del dictionary[key]
    return dictionary
"""

# Wersja 2


def removeFromDictionary(dictionary, key):
    if key not in dictionary:
        return dictionary
    else:
        del dictionary[key]
        return dictionary


dict1 = {1, 2, 3, 4, 5, 6}
key1 = 3
print(removeFromDictionary(dict1, key1))
