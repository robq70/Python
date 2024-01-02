"""
Atrybuty klasy - ćwiczenie
Wprowadzenie:
Jesteś menedżerem nowo otwartego muzeum sztuki. Twoim zadaniem jest stworzenie systemu do zarządzania kolekcją obrazów w muzeum. Każdy obraz posiada tytuł, autora oraz rok powstania.
Punkty, które ma zrealizować wykonujący zadanie:
1. Utwórz klasę Museum z następującymi atrybutami:
    - name (nazwa muzeum)
    - collection (początkowo pusta lista obrazów)
2. Dodaj konstruktor __init__, który przyjmuje nazwę muzeum i inicjuje atrybuty klasy.
3. Dodaj metodę addPainting, która przyjmuje tytuł obrazu, autora oraz rok powstania i dodaje obraz do kolekcji.
4. Dodaj metodę showCollection, która wyświetla wszystkie obrazy w kolekcji wraz z ich detalami.
5. Dodaj metodę countPaintings, która zwraca liczbę obrazów w kolekcji.
6. Utwórz instancję klasy Museum o nazwie "Muzeum Narodowe".
7. Dodaj kilka obrazów do kolekcji za pomocą metody addPainting.
8. Wykorzystaj metodę showCollection do wyświetlenia obrazów w kolekcji.
Podpowiedź:
Pamiętaj o dodaniu self jako pierwszego argumentu dla wszystkich metod w klasie.
"""


class Museum:
    def __init__(self, name):
        self.name = name
        self.collection = []

    def addPainting(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.collection.append({"title": title, "author": author, "year": year})

    def showCollection(self):
        for painting in self.collection:
            print(
                f"Title: {painting['title']}, Autor: {painting['author']}, Year: {painting['year']}"
            )

    def countPaintings(self):
        return len(self.collection)


nationalMuseum = Museum("Muzeum Narodowe")
nationalMuseum.addPainting("Dama z lasiczka", "Van Gogh", 1450)
nationalMuseum.addPainting("Widok z Madrytu", "Da Vinci", 1650)
nationalMuseum.addPainting("Bitwa pod Vienna", "Bocelli", 1750)
nationalMuseum.showCollection()
print(nationalMuseum.countPaintings())
