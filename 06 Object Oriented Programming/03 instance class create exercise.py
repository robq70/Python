"""
Tworzenie instancji obiektów na bazie klasy - zadanie
Wprowadzenie:
Klasy w Pythonie służą do definiowania obiektów i zachowań związanych z tymi obiektami. W tym zadaniu skupimy się na tworzeniu klasy Radio, która będzie reprezentować radio oraz na tworzeniu instancji tej klasy.
Kroki do wykonania:
1. Utwórz klasę Radio.
2. W konstruktorze klasy Radio (__init__), zainicjuj atrybuty: brand, frequency oraz volume na podstawie przekazanych argumentów. Dodatkowo, dodaj atrybut isOn z domyślną wartością False, który będzie informować, czy radio jest włączone.
3. Dodaj metodę turnOn, która ustawi atrybut isOn na True.
4. Dodaj metodę turnOff, która ustawi atrybut isOn na False.
5. Dodaj metodę getRadioInfo, która zwróci informacje o radiu w formacie: "Marka: [brand], Częstotliwość: [frequency] MHz, Głośność: [volume]".
6. Utwórz dwie instancje klasy Radio:
    - Pierwsza o nazwie radio1 z atrybutami: brand="Sony", frequency=101.2, volume=5.
    - Druga o nazwie radio2 z atrybutami: brand="Philips", frequency=98.7, volume=7.
Podpowiedź:
Aby zainicjować atrybuty w konstruktorze klasy, użyj self.brand = brand, self.frequency = frequency oraz self.volume = volume.
"""


class Radio:
    def __init__(self, brand, frequency, volume):
        self.brand = brand
        self.frequency = frequency
        self.volume = volume
        self.isOn = False

    def turnOn(self):
        self.isOn = True

    def turnOff(self):
        self.isOn = False

    def getRadioInfo(self):
        return f"Marka: {self.brand}, Częstotliwość: {self.frequency} MHz, Głośność: {self.volume}"


radio1 = Radio("Sony", 101.2, 5)
print(radio1.getRadioInfo())
radio2 = Radio("Philips", 98.7, 7)
print(radio2.getRadioInfo())
