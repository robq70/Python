"""Konwersja czasu z formatu 24-godzinnego na 12-godzinny.
Wprowadzenie:
Masz daną godzinę w formacie 24-godzinnym jako ciąg znaków. Twoim zadaniem jest napisanie funkcji, która przekształci tę godzinę na format 12-godzinny.
Punkty:
1. Utwórz funkcję o nazwie convertTo12HourFormat.
2. Funkcja powinna przyjmować jeden argument: time24 (ciąg znaków reprezentujący godzinę w formacie HH:MM).
3. Funkcja powinna zwrócić godzinę w formacie 12-godzinnym z dopiskiem AM lub PM.
4. Jeśli podany ciąg znaków jest nieprawidłowy, funkcja powinna zwrócić "Nieprawidłowy format".
Podpowiedź:
Rozważ podział ciągu znaków na godziny i minuty, a następnie przekształcenie godziny na format 12-godzinny."""


def convertTo12HourFormat(time24):
    if len(time24) != 5 or time24[2] != ":":
        return "Nieprawidłowy format"

    hours, minutes = map(int, time24.split(":"))

    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        return "Nieprawidłowy format"

    if hours == 0:
        return f"12:{minutes:02d} AM"
    elif hours < 12:
        return f"{hours}:{minutes:02d} AM"
    elif hours == 12:
        return f"12:{minutes:02d} PM"
    else:
        return f"{hours-12}:{minutes:02d} PM"


# 02d oznacza że nawet jeśli jest 00 to nie można go skracać do formatu 0

times = "13:00"
print(convertTo12HourFormat(times))
