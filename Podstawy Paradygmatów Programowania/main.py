def validate_pesel(pesel):
    if len(pesel) != 11:
        return False

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
    checksum = sum(int(pesel[i]) * weights[i] for i in range(11)) % 10

    if checksum != 0:
        return False

    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    if month > 80:
        year += 1800
        month -= 80
    elif month > 60:
        year += 2200
        month -= 60
    elif month > 40:
        year += 2100
        month -= 40
    elif month > 20:
        year += 2000
        month -= 20
    else:
        year += 1900

    print("Data urodzenia: {day}.{month}.{year}".format(day=day, month=month, year=year))
    return True

# Przykładowe użycie
pesel_number = input("Podaj numer PESEL: ")
if validate_pesel(pesel_number):
    print("Numer PESEL jest poprawny.")
else:
    print("Numer PESEL jest niepoprawny.")
