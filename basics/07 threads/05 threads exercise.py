"""
Ćwiczenie z klasą Thread
Wprowadzenie:
W tym zadaniu Twoim celem będzie napisanie klasy, która rozszerza klasę Thread. Wewnątrz tej klasy, w metodzie run, powinna być obliczona suma liczb od 1 do 25. Po zakończeniu obliczeń, suma powinna być wyświetlona w konsoli.
Kroki do wykonania:
1. Zaimportuj odpowiedni moduł do pracy z wątkami w Pythonie.
2. Zdefiniuj klasę SumThread, która rozszerza klasę Thread.
3. Wewnątrz klasy SumThread, zdefiniuj metodę run. W tej metodzie oblicz sumę liczb od 1 do 25.
4. Po obliczeniu sumy, wyświetl ją w konsoli.
5. Po zdefiniowaniu klasy, utwórz jej instancję i uruchom wątek.
Podpowiedź:
Możesz użyć wbudowanej funkcji sum oraz funkcji range do obliczenia sumy liczb.
"""

import threading


class SumThread(threading.Thread):
    def run(self):
        suma = 0
        for i in range(1, 26):
            suma = suma + i
        print(suma)

    # kod metody


print()
t1 = SumThread()
t1.start()
t1.join()
# uwtorzenie nowej instancji i wystartowanie wątku


"""
Metoda 2
import threading

class SumThread(threading.Thread):
    def run(self):
        totalSum = sum(range(1, 26))
        print(totalSum)
 
thread = SumThread()
thread.start()

"""
