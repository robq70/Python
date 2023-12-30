import validators


def valPhone(number):
    if len(number) == 11:
        return number[0] == "4" and number[1] == "8" and number.isdigit()
    else:
        return False


phoneInput = "48793101252"
print(valPhone(phoneInput))
