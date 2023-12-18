"""
Mutowalność argumentów funkcji

Wprowadzenie:

W Pythonie, gdy przekazujemy mutowalne obiekty, takie jak listy czy słowniki, do funkcji, przekazujemy je "przez referencję". Oznacza to, że jeśli zmienimy wartość argumentu wewnątrz funkcji, wpłynie to na pierwotny obiekt poza funkcją. W tym zadaniu zrozumiesz, jak działa mutowalność argumentów w Pythonie, wykonując operacje na słownikach.

Kroki do wykonania:

    Utwórz słownik opisujący pracownika i zapisz go w zmiennej employee. Słownik powinien zawierać klucze: name, email, rank (z wartością "programmer") oraz salary (z wartością 8000).

    Napisz funkcję o nazwie promoteToManager, która przyjmuje parametr user, będący słownikiem.

    Wewnątrz funkcji sprawdź, czy wartość klucza rank w słowniku user to "manager". Jeśli tak, wydrukuj komunikat "Pracownik jest już managerem" i zakończ działanie funkcji.

    Jeśli wartość klucza rank nie jest "manager", zmień ją na "manager" i podnieś wartość klucza salary o 50%.

    Poza funkcją wywołaj promoteToManager, przekazując jako argument słownik employee.

    Wydrukuj w konsoli słownik employee i zobacz, czy został on zaktualizowany.

Podpowiedź: Aby podnieść wartość salary o 50%, możesz użyć operacji user["salary"] *= 1.5.
"""

employee = {
    "name": "Adam",
    "email": "adam@example.com",
    "rank": "programmer",
    "salary": 8000,
}


def promoteToManager(user):
    if user["rank"] == "manager":
        print("Pracownik jest już managerem")
        return
    user["rank"] = "manager"
    user["salary"] *= 1.5


promoteToManager(employee)
print(employee)
