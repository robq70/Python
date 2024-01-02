"""
Ćwiczenie z metodami klasy
Wprowadzenie:
Jesteś redaktorem naczelnym gazety i chcesz stworzyć system do zarządzania artykułami. Twoim zadaniem jest stworzenie klasy Newspaper, która pozwoli na dodawanie artykułów oraz wyświetlanie ich listy.
Punkty do wykonania przez uczestnika:
1. Utwórz klasę Newspaper z następującymi atrybutami i metodami:
    - articles: lista przechowująca artykuły. Każdy artykuł to słownik z kluczami "title" (tytuł artykułu) i "content" (treść artykułu).
    - addArticle(self, title, content): metoda dodająca artykuł do listy articles.
    - printArticles(self): metoda wyświetlająca wszystkie artykuły w formacie: "Tytuł: [title], Treść: [content]".
    - getNumberOfArticles(self): metoda zwracająca liczbę artykułów w gazecie.
2. Utwórz instancję klasy Newspaper o nazwie dailyNews.
3. Dodaj dwa artykuły do dailyNews za pomocą metody addArticle.
4. Wykorzystaj metodę printArticles, aby wyświetlić dodane artykuły.
Podpowiedź:
Pamiętaj o inicjalizacji listy articles w konstruktorze klasy. Aby dodać nowy artykuł, możesz użyć metody append na liście.
"""


class Newspaper:
    def __init__(self):
        self.articles = []

    def addArticle(self, title, content):
        self.articles.append({"title": title, "content": content})

    def printArticles(self):
        for article in self.articles:
            print(f"Tytuł: {article['title']}, Treść: {article['content']}")

    def getNumberOfArticles(self):
        return len(self.articles)


dailyNews = Newspaper()
dailyNews.addArticle("Nowy dzień", "Dzisiaj jest nowy dzień")
dailyNews.addArticle("Stary dzień", "Dzisiaj jest stary dzień")
dailyNews.addArticle("Stary dzień", "Dzisiaj jest stary dzień")
dailyNews.addArticle("Stary dzień", "Dzisiaj jest stary dzień")
dailyNews.printArticles()
print(dailyNews.getNumberOfArticles())
