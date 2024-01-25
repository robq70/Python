"""
Konwersja między litrami a galonami

Wprowadzenie:
Często podczas podróży między krajami musimy dokonywać konwersji jednostek miary. W tym zadaniu skupimy się na konwersji między litrami a galonami.

Punkty do wykonania:
1. Napisz funkcję litersToGallons(), która przyjmuje liczbę reprezentującą ilość litrów i zwraca jej odpowiednik w galonach, musisz też zaokrąglić wynik do dwóch miejsc po przecinku.
2. Napisz funkcję gallonsToLiters(), która przyjmuje liczbę reprezentującą ilość galonów i zwraca jej odpowiednik w litrach, musisz też zaokrąglić wynik do dwóch miejsc po przecinku.
3. Oba przeliczniki powinny być dokładne do dwóch miejsc po przecinku.

Podpowiedź:
1 galon amerykański to około 3.78541 litra."""

# 1 Opcja
"""
def litersToGallons(liters):
    return round(liters / 3.78541, 2)
    
def gallonsToLiters(gallons):
    return round(gallons * 3.78541, 5)
"""

# 2 Opcja


def litersToGallons(liters):
    return "{:.2f}".format(3.78541 * liters)


def gallonsToLiters(liters):
    return "{:.2f}".format(liters / 3.78541)


litrOn = 1
print(litersToGallons(litrOn))
print(gallonsToLiters(litrOn))
