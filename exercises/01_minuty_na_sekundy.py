"""
Ćwiczenie nr 1
Wprowadzenie:
Często w codziennym życiu potrzebujemy przeliczać jednostki czasu. Jednym z podstawowych przeliczeń jest konwersja minut na sekundy. Twoim zadaniem będzie napisanie funkcji, która dokona tej konwersji.
Punkty do wykonania:
1. Utwórz funkcję o nazwie minutyNaSekundy.
2. Funkcja powinna przyjmować jeden argument - liczbę minut.
3. Funkcja powinna zwracać odpowiednią liczbę sekund.
4. Pamiętaj, że 1 minuta to 60 sekund.
Podpowiedź:
Aby przeliczyć minuty na sekundy, pomnóż liczbę minut przez 60.
"""


def minutyNaSekundy(minutes):
    return minutes * 60


seconds = minutyNaSekundy(5)
print("Ilość godzin:", seconds)
