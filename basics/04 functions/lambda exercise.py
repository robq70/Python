"""
Wprowadzenie:
W Pythonie funkcje lambda to małe, anonimowe funkcje, które można zdefiniować w jednym wierszu. Są one używane tam, gdzie potrzebujemy krótkiej funkcji na krótki czas i nie chcemy definiować pełnej funkcji za pomocą def. W tym zadaniu nauczysz się, jak tworzyć i używać funkcji lambda.
Kroki do wykonania:
1. Utwórz listę liczb o nazwie numbers z wartościami od 1 do 10.
2. Używając funkcji filter() i funkcji lambda, stwórz nową listę evenNumbers, która będzie zawierać tylko parzyste liczby z listy numbers.
3. Używając funkcji map() i funkcji lambda, stwórz nową listę squaredNumbers, która będzie zawierać kwadraty liczb z listy numbers.
4. Wydrukuj listy evenNumbers i squaredNumbers.
Podpowiedź:
Funkcja lambda ma składnię: lambda arguments: expression. Pamiętaj, że funkcja lambda może mieć dowolną liczbę argumentów, ale tylko jedno wyrażenie.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenNumbers = list(filter(lambda x: x % 2 == 0, numbers))

squaredNumbers = list(map(lambda a: a**2, numbers))

print(f"Parzyste liczby: {evenNumbers}")
print(f"Kwadraty liczb: {squaredNumbers}")
