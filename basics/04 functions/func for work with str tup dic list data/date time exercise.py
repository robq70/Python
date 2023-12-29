"""
Ćwiczenie z datami
Wprowadzenie:
W tym zadaniu Twoim celem będzie napisanie funkcji, która na podstawie daty urodzenia osoby określi, czy osoba ta ma co najmniej 18 lat i może przystąpić do egzaminu na prawo jazdy.
Kroki do wykonania:
1. Zdefiniuj funkcję o nazwie canTakeDrivingTest, która przyjmie jeden parametr: birthDate (data urodzenia osoby w formacie "YYYY-MM-DD").
2. Funkcja powinna obliczyć, ile lat minęło od daty urodzenia do obecnej daty.
3. Jeśli osoba ma co najmniej 18 lat, funkcja powinna zwrócić True, w przeciwnym razie False.
Podpowiedź:
Możesz użyć modułu datetime w Pythonie, aby pracować z datami i obliczać różnicę w latach.
"""

from datetime import datetime


def canTakeDrivingTest(birthDate):
    # Rozwiązanie tutaj
    currentDate = datetime.now()
    birthDateObj = datetime.strptime(birthDate, "%Y-%m-%d")
    
    age = currentDate.year - birthDateObj.year - ((currentDate.month, currentDate.day) < (birthDateObj.month, birthDateObj.day))
 
    return age >= 18