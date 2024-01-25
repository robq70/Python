"""Ćwiczenie nr 15

Konwersja temperatury z Celsiusza na Fahrenheita.
Wprowadzenie:
Często podczas podróży między krajami musimy dostosować się do różnych jednostek miar. Jednym z takich przykładów jest konwersja temperatury. Twoim zadaniem jest napisanie funkcji, która przekształci temperaturę z stopni Celsiusza na stopnie Fahrenheita.
Punkty:
1. Utwórz funkcję o nazwie celsiusToFahrenheit.
2. Funkcja powinna przyjmować jeden argument: tempCelsius (temperatura w stopniach Celsiusza).
3. Funkcja powinna zwrócić temperaturę w stopniach Fahrenheita.
4.Wykorzystaj wzór: F =  C * 9/5 + 32, gdzie F to temperatura w stopniach Fahrenheita, a C to temperatura w stopniach Celsiusza.
Podpowiedź:
Upewnij się, że dokładnie przekształcasz wartość według podanego wzoru."""


def celsiusToFahrenheit(tempCelsius):
    return tempCelsius * 9 / 5 + 32


celsius = 10
print(celsiusToFahrenheit(celsius))
