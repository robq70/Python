"""
Ćwiczenie z klasą i konstruktorem
Wprowadzenie:
Klasy w Pythonie służą do definiowania obiektów i zachowań związanych z tymi obiektami. W tym zadaniu będziesz tworzyć klasę PassengerPlane, która będzie reprezentować samolot pasażerski.
Kroki do wykonania:
1. Utwórz klasę PassengerPlane.
2. W konstruktorze klasy PassengerPlane (__init__), zainicjuj atrybuty: brand, capacity (pojemność - liczba miejsc dla pasażerów) oraz currentPassengers (aktualna liczba pasażerów) na podstawie przekazanych argumentów. Dodatkowo, dodaj atrybut isFlying z domyślną wartością False, który będzie informować, czy samolot jest w powietrzu.
3. Dodaj metodę takeOff, która ustawi atrybut isFlying na True.
4. Dodaj metodę land, która ustawi atrybut isFlying na False.
5. Dodaj metodę boardPassengers, która przyjmuje liczbę pasażerów do wejścia na pokład i zwiększa wartość currentPassengers. Jeśli liczba pasażerów przekroczy pojemność, wydrukuj komunikat o braku miejsc.
6. Dodaj metodę getPlaneInfo, która zwróci informacje o samolocie w formacie: "Marka: [brand], Pojemność: [capacity], Aktualna liczba pasażerów: [currentPassengers]".
7. Utwórz dwie instancje klasy PassengerPlane:
    - Pierwsza o nazwie plane1 z atrybutami: brand="Boeing", capacity=200, currentPassengers=150.
    - Druga o nazwie plane2 z atrybutami: brand="Airbus", capacity=250, currentPassengers=100.
Podpowiedź:
Aby zainicjować atrybuty w konstruktorze klasy, użyj self.brand = brand, self.capacity = capacity oraz self.currentPassengers = currentPassengers.

"""


class PassengerPlane:
    def __init__(
        self,
        brand,
        capacity,
        currentPassengers,
    ):
        self.brand = brand
        self.capacity = capacity
        self.currentPassengers = currentPassengers
        self.isFlying = False

    def takeOff(self):
        self.isFlying = True

    def land(self):
        self.isFlying = False

    def boardPassengers(self, number):
        if self.currentPassengers + number <= self.capacity:
            self.currentPassengers += number
        else:
            print("Brak miejsc!")

    def getPlaneInfo(self):
        return f"Marka: {self.brand}, Pojemność: {self.capacity}, Aktualna liczba pasażerów: {self.currentPassengers}"


plane1 = PassengerPlane("Boeing", 200, 150)
plane2 = PassengerPlane("Airbus", 250, 100)
