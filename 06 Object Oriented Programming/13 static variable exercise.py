"""
Ćwiczenie z statyczną zmienną
Wprowadzenie:
Jesteś programistą w dużym mieście, które chce zautomatyzować system zarządzania biblioteką. Każda książka w bibliotece ma tytuł, autora i status dostępności. Dodatkowo, biblioteka chce śledzić, ile razy książki były wypożyczane.
Punkty, które ma zrealizować wykonujący zadanie:
1. Utwórz klasę Book z następującymi atrybutami:
    - title (tytuł książki)
    - author (autor książki)
    - isAvailable (status dostępności książki, domyślnie True)
    - loanCount (statyczna zmienna śledząca liczbę wszystkich wypożyczeń)
2. Dodaj konstruktor __init__, który przyjmuje tytuł i autora książki i inicjuje je.
3. Dodaj metodę borrowBook, która zmienia status dostępności książki na False i zwiększa licznik wypożyczeń o 1.
4. Dodaj metodę returnBook, która zmienia status dostępności książki na True.
5. Dodaj destruktor __del__, który wyświetla komunikat o tym, że książka została usunięta z systemu.
6. Dodaj statyczną metodę totalLoans, która zwraca łączną liczbę wypożyczeń.
Podpowiedź:
Aby utworzyć statyczną zmienną w klasie, zdefiniuj ją przed konstruktorem. Statyczne metody można zdefiniować za pomocą dekoratora @staticmethod.
"""


class Book:
    loanCount = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.isAvailable = True

    def borrowBook(self):
        if self.isAvailable:
            self.isAvailable = False
            Book.loanCount += 1

    def returnBook(self):
        self.isAvailable = True

    @staticmethod
    def totalLoans():
        return Book.loanCount

    def __del__(self):
        print(f"Książka '{self.title}' została usunięta z systemu")
