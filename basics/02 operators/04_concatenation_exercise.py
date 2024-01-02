"""
Konkatenacja ciągów znaków w Pythonie
Wprowadzenie:
Konkatenacja to proces łączenia dwóch lub więcej ciągów znaków w jeden. W Pythonie konkatenację ciągów znaków można osiągnąć za pomocą operatora +. W tym zadaniu nauczysz się łączyć różne ciągi znaków w jeden dłuższy ciąg.
Kroki do wykonania:
1. Utwórz trzy zmienne tekstowe: firstName, lastName i title z wartościami "John", "Doe" i "Dr." odpowiednio.
2. Używając operatora +, połącz te trzy zmienne w jeden ciąg znaków o nazwie fullName, taki że przed imieniem i nazwiskiem będzie tytuł, a między imieniem a nazwiskiem będzie spacja.
3. Wydrukuj wartość zmiennej fullName.
Podpowiedź:
Pamiętaj o dodaniu odpowiednich spacji podczas łączenia ciągów znaków, aby wynikowy ciąg był czytelny.
Oczekiwany wynik w konsoli:
    Dr. John Doe
"""

firstName = ("John", "Doe")
lastName = "Dr."
fullName = lastName + " " + firstName[0] + " " + firstName[1]
print(fullName)
