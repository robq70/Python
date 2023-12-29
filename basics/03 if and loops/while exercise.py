"""
Ćwiczenie z kodowania z pętlą while
Wprowadzenie:
Często zdarza się, że chcemy przetworzyć listę w odwrotnej kolejności. W tym zadaniu nauczysz się, jak używać pętli while do wyświetlania elementów listy od końca do początku.
Kroki do wykonania:
1. Zdefiniuj listę names zawierającą imiona: "Ania", "Ola", "Kasia", "Daniel".
2. Utwórz zmienną i i przypisz jej wartość długości listy names pomniejszonej o 1. Będzie to indeks ostatniego elementu listy.
3. Utwórz pętlę while, która będzie działać dopóki wartość i jest większa lub równa 0.
4. W ciele pętli przypisz do zmiennej person imię z listy names o indeksie i.
5. Wydrukuj wartość zmiennej person.
6. Zmniejsz wartość i o 1.
Podpowiedź:
Pamiętaj, że indeksowanie w Pythonie zaczyna się od 0, więc ostatni element listy ma indeks równy długości listy pomniejszonej o 1.
"""

names = ["Ania", "Ola", "Kasia", "Daniel"]
# napisz poniżej resztę kodu
i = len(names) - 1

while i >= 0:
    person = names[i]
    print(person)
    i -= 1
