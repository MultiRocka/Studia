from math import radians, cos, sin, asin, sqrt


class Punkt:
    def __init__(self, nazwa, x, y):
        self.nazwa = nazwa
        self.x = x
        self.y = y


def dodaj(nazwa=None):
    if nazwa is None:
        nazwa = input("Podaj nazwę punktu: ")
    x = float(input("Podaj koordynat x: "))
    y = float(input("Podaj koordynat y: "))

    with open("dane.txt", "r") as plik:
        lines = plik.readlines()

    found = False

    for i, line in enumerate(lines):
        parts = line.split(" - ")
        if len(parts) > 1 and parts[0] == nazwa:
            lines[i] = f"{nazwa} - {x}, {y}\n"
            found = True
            break

    if not found:
        lines.append(f"{nazwa} - {x}, {y}\n")

    with open("dane.txt", "w") as plik:
        plik.writelines(lines)

    if found:
        print("Zaktualizowano istniejący punkt.")
    else:
        print("Dodano nowy punkt.")


def findxy():
    nazwa = input("Podaj nazwe szukanego punktu: ").lower()

    found = False
    cord = None

    with open("dane.txt", "r") as plik:
        for line in plik:
            if nazwa in line.lower():
                found = True
                cord = line.split(" - ")[1].strip()
                break

    if found:
        print(f"\nSzukane koordynaty dla punktu {nazwa} to : {cord} \n")
    else:
        print("BRAK PUNKTU W PLIKU, CZY CHCESZ DODAĆ PUNKT?")
        resp = input("1.tak 2.nie \n")
        if resp == '1':
            dodaj(nazwa)
        elif resp == '2':
            main()


def haversine(lon1, lat1, lon2, lat2):
    """
     Calculate the great circle distance between two points
     on the earth (specified in decimal degrees)
     """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2,
                                           lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon /
                                                         2) ** 2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers is 6371
    meters = 6371000 * c
    return meters


def sortuj_punkty(punkty, ref_x, ref_y):
    sorted_punkty = sorted(punkty, key=lambda p: haversine(ref_x, ref_y, p.x, p.y))
    return sorted_punkty


def wyswietl_posortowane_punkty(punkty):
    for punkt in punkty:
        print(f"{punkt.nazwa} - {punkt.x}, {punkt.y}")


def main():
    while True:
        punkty = []
        with open("dane.txt", "r") as plik:
            for line in plik:
                parts = line.split(" - ")
                nazwa = parts[0]
                x, y = map(float, parts[1].split(","))
                punkt = Punkt(nazwa, x, y)
                punkty.append(punkt)

        print("Co chcesz zrobić?")
        print("0. Zakończ program")
        print("1. Dodaj punkt geograficzny")
        print("2. Znajdź współrzędne na podstawie nazwy")
        print(
            "3. Wyświetl wszystkie punkty w kolejności od najbliższego do najdalszego od współrzędnych: Pentagon - "
            "51.235369, 22.553145")

        wybor = input("Twój wybór: ")

        if wybor == "0":
            print("koniec programu.")
            break
        elif wybor == "1":
            dodaj()
        elif wybor == "2":
            findxy()
        elif wybor == "3":
            ref_x = 51.235369
            ref_y = 22.553145
            posortowane_punkty = sortuj_punkty(punkty, ref_x, ref_y)
            print("\n")
            wyswietl_posortowane_punkty(posortowane_punkty)
            print("\n")


main()
