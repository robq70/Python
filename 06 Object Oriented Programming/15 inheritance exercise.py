"""
Dziedziczenie - ćwiczenie
Wprowadzenie:
Jesteś programistą w firmie produkującej różne rodzaje pojazdów. Twoim zadaniem jest stworzenie modelu obiektowego, który opisuje ogólną kategorię pojazdów oraz bardziej szczegółową kategorię samochodów.
Zadania do wykonania:
1. Utwórz klasę Vehicle z następującymi atrybutami: brand (marka) i yearOfProduction (rok produkcji).
2. Dodaj konstruktor do klasy Vehicle, który przyjmuje markę i rok produkcji jako argumenty.
3. Dodaj metodę displayInfo do klasy Vehicle, która wyświetla informacje o pojeździe.
4. Utwórz klasę Car, która dziedziczy po klasie Vehicle.
5. Dodaj do klasy Car atrybut model.
6. Rozszerz konstruktor klasy Car tak, aby przyjmował również model samochodu jako argument.
7. Nadpisz metodę displayInfo w klasie Car tak, aby wyświetlała również model samochodu.
8. Dodaj destruktor do klasy Vehicle, który wyświetla komunikat o usunięciu obiektu.
Podpowiedź:
Pamiętaj o używaniu słowa kluczowego super() podczas dziedziczenia atrybutów i metod z klasy nadrzędnej.
"""

class Vehicle:
    def __init__(self, brand, yearOfProduction):
        self.brand = brand
        self.yearOfProduction = yearOfProduction

    def displayInfo(self):
        print(f"Brand: {self.brand}, Year of production: {self.yearOfProduction}")

    def __del__(self):
        print(f"Obiekt {self.brand} został usunięty")


class Car(Vehicle):
    def __init__(self, brand, yearOfProduction, model):
        super().__init__(brand, yearOfProduction)
        self.model = model

    def displayInfo(self):
        super().displayInfo()
        print(f"Model: {self.model}")


vehicle1 = Vehicle("Ford", 2023)
vehicle1.displayInfo()
car1 = Car("Fiat", 2022, "Tipo")
car1.displayInfo()
