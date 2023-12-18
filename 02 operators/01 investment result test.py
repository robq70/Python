capital = 5000
rateOfInterest = 0.08  # 8%
inflationRate = 0.15  # 15%

earnedMoney = capital * rateOfInterest
print("Zarobiona kwota: ", earnedMoney)
lostMoney = capital * inflationRate
print("Utracona kwota: ", lostMoney)
newCapital = capital + earnedMoney - lostMoney
print("Kwota końcowa: ", newCapital)
