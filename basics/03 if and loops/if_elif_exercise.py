"""
Ćwiczenie z kodowania z if elif
Wprowadzenie:
W tym zadaniu zostaniesz wprowadzony w podstawy instrukcji warunkowych w Pythonie. Twoim zadaniem będzie klasyfikacja wartości liczbowej na podstawie jej wielkości.
Kroki do wykonania:
1. Zdefiniuj globalną zmienną number i przypisz jej wartość 35, dodaj też zmienną classification w której zapiszesz wynik działania kodu.
2. Używając instrukcji if, sprawdź czy wartość number jest mniejsza niż 10. Jeśli tak, przypisz zmiennej classification wartość "Mała liczba".
3. Używając instrukcji elif, sprawdź czy wartość number jest co najmniej 10, ale mniejsza niż 50. Jeśli tak, przypisz zmiennej classification wartość "Średnia liczba".
4. W przeciwnym razie, używając instrukcji else, przypisz zmiennej classification wartość "Duża liczba".
Podpowiedź: Pamiętaj, że instrukcje elif i else są opcjonalne i możesz ich używać w zależności od potrzeb.
"""
number = 35
classification = ""

# Poniżej zapisz if elif
if number < 10:
    classification = "Mała liczba"
elif number >= 10 and number < 50:
    classification = "Średnia liczba"
else:
    classification = "Duża liczba"
