"""
Nazwane argumenty funkcji - zadanie

Wprowadzenie:

W Pythonie, podczas wywoływania funkcji, możemy używać nazwanych argumentów, co pozwala na przekazywanie wartości w dowolnej kolejności oraz zwiększa czytelność kodu. W tym zadaniu nauczysz się, jak korzystać z nazwanych argumentów podczas wywoływania funkcji.

Kroki do wykonania:

    Napisz funkcję o nazwie displayPersonDetails, która przyjmuje trzy argumenty: name, age oraz city.

    Funkcja powinna zwracać łańcuch znaków w formacie: "{name} ma {age} lat i mieszka w {city}."

    Wywołaj funkcję displayPersonDetails trzykrotnie:

        Pierwsze wywołanie używając tylko pozycyjnych argumentów (np. "Anna", 25, "Warszawa").

        Drugie wywołanie używając nazwanych argumentów w dowolnej kolejności (np. city="Kraków", name="Tomasz", age=30).

        Trzecie wywołanie mieszając argumenty pozycyjne i nazwane (np. "Karol", city="Poznań", age=28).

    Wydrukuj wyniki każdego wywołania w konsoli.

Podpowiedź:

Aby użyć nazwanego argumentu podczas wywoływania funkcji, użyj nazwy argumentu, a następnie przypisz mu wartość, np. funkcja(arg1=wartość1, arg2=wartość2).


Oczekiwane dane w konsoli po uruchomieniu programu:

    Anna ma 25 lat i mieszka w Warszawa.

    Tomasz ma 30 lat i mieszka w Kraków.

    Karol ma 28 lat i mieszka w Poznań.
"""


def displayPersonDetails(name, age, city):
    return f"{name} ma {age} lat i mieszka w {city}."


print(displayPersonDetails("Anna", 25, "Warszawa"))
print(displayPersonDetails(city="Kraków", name="Tomasz", age=30))
print(displayPersonDetails("Karol", city="Poznań", age=28))
