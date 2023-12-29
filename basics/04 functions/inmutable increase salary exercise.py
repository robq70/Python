"""
Niemutowalność argumentów w funkcji

Wprowadzenie:

W Pythonie, gdy przekazujemy argumenty do funkcji, przekazujemy je "przez wartość". Oznacza to, że jeśli zmienimy wartość argumentu wewnątrz funkcji, nie wpłynie to na pierwotną zmienną poza funkcją. W tym zadaniu zrozumiesz, jak działa niemutowalność argumentów w Pythonie, wykonując operacje na liczbach całkowitych.

Kroki do wykonania:

    Napisz funkcję o nazwie increaseSalary z dwoma parametrami: money oraz bonus.

    Wewnątrz funkcji zwiększ wartość money o 20%.

    Następnie zwróć sumę money i bonus.

    Poza funkcją, utwórz zmienną salary o wartości 5000.

    Wywołaj funkcję increaseSalary, przekazując jako argumenty salary oraz 1000 jako bonus. Przypisz zwracaną wartość do zmiennej newSalary.

    Wydrukuj w konsoli wartości salary i newSalary.

Podpowiedź:

Aby zwiększyć wartość money o 20%, możesz użyć operacji money += money * 0.20.
"""
# Napisz tutaj rozwiązanie


def increaseSalary(money, bonus):
    money += money * 0.20
    return money + bonus


salary = 5000

newSalary = increaseSalary(salary, 1000)

print(salary)
print(newSalary)
