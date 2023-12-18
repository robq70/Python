age = int(input("Podaj swój wiek - "))
weight = int(input("Podaj swoją wagę - "))

if age >= 18:
    if weight >= 50:
        print("Kandydat może oddać krew")
    else:
        print("Kandydat nie spełnia kryterium wagi")
else:
    print("Kandydat nie spełnia kryterium wieku")
