"""
Destruktor klasy - ćwiczenie
Wprowadzenie:
Jesteś programistą w firmie produkującej komputery. Twoim zadaniem jest stworzenie systemu do zarządzania zasobami komputera. Każdy komputer posiada nazwę modelu, ilość pamięci RAM oraz pojemność dysku twardego.
Punkty, które ma zrealizować wykonujący zadanie:
1. Utwórz klasę Computer z następującymi atrybutami:
    - modelName (nazwa modelu komputera)
    - ram (ilość pamięci RAM w GB)
    - storage (pojemność dysku twardego w GB)
2. Dodaj konstruktor __init__, który przyjmuje wszystkie atrybuty klasy i inicjuje je.
3. Dodaj metodę showSpecs, która wyświetla specyfikację komputera.
4. Dodaj metodę upgradeRAM, która przyjmuje ilość GB i zwiększa ilość pamięci RAM o podaną wartość.
5. Dodaj destruktor __del__, który wyświetla komunikat o tym, że obiekt został usunięty.
Podpowiedź:
Pamiętaj o dodaniu self jako pierwszego argumentu dla wszystkich metod w klasie. Dla destruktora nie przekazuj żadnych dodatkowych argumentów poza self.
"""


class Computer:
    def __init__(self, modelName, ram, storage):
        self.modelName = modelName
        self.ram = ram
        self.storage = storage

    def showSpecs(self):
        print(
            f"Model: {'self.modelName'}, Ram: {'self.ram'}, Storage: {'self.storage'}GB"
        )

    def upgradeRAM(self, addram):
        self.ram += addram

    def __del__(self):
        print(f"Komputer {self.modelName} został usunięty.")
