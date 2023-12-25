"""
Ćwiczenie z tworzniem klasy
Wprowadzenie:
Klasy w Pythonie są podstawowym narzędziem do tworzenia obiektów. W tym zadaniu skupimy się na tworzeniu klasy Book, która będzie przechowywać informacje o książce i jej rozdziałach.
Kroki do wykonania:
1. Utwórz klasę Book.
2. W konstruktorze klasy Book (__init__), zainicjuj pustą listę chapters.
3. Dodaj metodę addChapter, która przyjmuje jako argument nazwę rozdziału i dodaje go do listy rozdziałów.
4. Dodaj metodę printChapters, która wydrukuje wszystkie rozdziały książki w konsoli.
5. Dodaj metodę getChaptersNum, która zwróci liczbę rozdziałów w książce.
Podpowiedź:
Aby zainicjować listę w konstruktorze klasy, użyj self.chapters = [].
"""

class Book:
    def __init__(self):
        self.chapters = []

    def addChapter(self, chapterName):
        self.chapters.append(chapterName)

    def printChapters(self):
        for chapter in self.chapters:
            print(chapter)

    def getChaptersNum(self):
        return len(self.chapters)


book1 = Book()
book1.addChapter("Rozdział 1")
book1.addChapter("Rozdział 2")
book1.addChapter("Rozdział 3")
book1.addChapter("Rozdział 4")
book1.printChapters()
print(book1.getChaptersNum())
