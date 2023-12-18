"""
Domyślne argumenty funkcji - zadanie

Wprowadzenie:

W Pythonie możemy określić domyślne wartości dla argumentów funkcji. Oznacza to, że jeśli podczas wywoływania funkcji nie podamy wartości dla takiego argumentu, zostanie użyta jego domyślna wartość. W tym zadaniu nauczysz się, jak korzystać z domyślnych argumentów w funkcji.

Kroki do wykonania:

    Napisz funkcję o nazwie greetUser, która przyjmuje dwa argumenty: name oraz greeting z domyślną wartością "Witaj".

    Funkcja powinna zwracać łańcuch znaków w formacie: "{greeting}, {name}!".

    Wywołaj funkcję greetUser trzykrotnie:

        Pierwsze wywołanie z jednym argumentem (np. "Anna").

        Drugie wywołanie z dwoma argumentami (np. "Tomasz" i "Cześć").

        Trzecie wywołanie bez argumentów.

    Wydrukuj wyniki każdego wywołania w konsoli.

Podpowiedź:

Aby zdefiniować domyślną wartość dla argumentu, użyj znaku równości po nazwie argumentu w definicji funkcji, np. def funkcja(arg1=default_value).


Oczekiwana odpowiedź w konsoli:

    Witaj, Anna!

    Cześć, Tomasz!

    Witaj, Gościu!

"""


def greetUser(name="Gościu", greeting="Witaj"):
    return f"{greeting}, {name}!"


print(greetUser("Anna"))
print(greetUser("Tomasz", "Cześć"))
print(greetUser())
