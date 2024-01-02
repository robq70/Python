"""
Ćwiczenie z tworzeniem wątku
Wprowadzenie:
W tym zadaniu Twoim celem będzie napisanie funkcji, która uruchomi nowy wątek. W tym wątku powinna działać pętla, która w pięciu iteracjach wyświetli kolejne wartości liczbowe w konsoli. Wątek powinien zostać zakończony po zakończeniu działania pętli.
Kroki do wykonania:
1. Zaimportuj odpowiedni moduł do pracy z wątkami w Pythonie.
2. Zdefiniuj funkcję displayValues - będzie to funkcja wywoływana w nowym wątku. Wewnątrz tej funkcji umieść pętlę, która pięć razy wyświetli kolejne wartości liczbowe (od 1 do 5) w konsoli z użyciem funkcji print() .
3. Zdefiniuj główną funkcję runThread - wewnątrz tej funkcji utwórz nowy wątek, który wywoła funkcję displayValues. Uruchom wątek i poczekaj na jego zakończenie.
Podpowiedź:
Możesz użyć modułu threading w Pythonie do pracy z wątkami. Pamiętaj o metodach start() i join() przy pracy z wątkami.
"""

import threading


def displayValues():
    for i in range(1, 6):
        print(i)

    # pętla
    # number = 1
    # while number < 6:
    #     print(number)
    #     number += 1


def runThread():
    thread = threading.Thread(target=displayValues)
    thread.start()
    thread.join()


print(displayValues())
