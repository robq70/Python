"""
Kolejne ćwiczenie z słownikiem
Wprowadzenie:
W tym zadaniu Twoim celem będzie napisanie funkcji, która sprawdzi, czy przekazany słownik z danymi nowo zarejestrowanego użytkownika jest prawidłowy. Słownik powinien zawierać informacje takie jak: nazwa użytkownika, adres email, wiek oraz ulubiony kolor.
Kroki do wykonania:
1. Zdefiniuj funkcję o nazwie validate_user_data, która przyjmie jeden parametr: user_data (słownik z danymi użytkownika).
2. Funkcja powinna sprawdzić, czy słownik zawiera wszystkie wymagane klucze: "username", "email", "age", "favorite_color". V
3. Adres email musi zawierać znak "@". V
4. Wiek musi być liczbą całkowitą.
5. Ulubiony kolor musi być jednym z następujących: "red", "blue", "white", "yellow", "green", "orange".
6. Jeśli wszystkie warunki są spełnione, funkcja powinna zwrócić True, w przeciwnym razie False.
Podpowiedź:
Możesz użyć operatora in do sprawdzenia, czy słownik zawiera określony klucz oraz funkcji isinstance() do sprawdzenia typu wartości.
"""


def validateUserData(userData):
    # Napisz tutaj rozwiązanie
    if not all(
        key in userData for key in ["username", "email", "age", "favoriteColor"]
    ):
        return False
    if "@" not in userData["email"]:
        return False
    if not isinstance(userData["age"], int):
        return False
    if userData["favoriteColor"] not in [
        "red",
        "blue",
        "white",
        "yellow",
        "green",
        "orange",
    ]:
        return False
    return True
