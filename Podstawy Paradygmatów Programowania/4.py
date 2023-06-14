import random
import string

def generate_license_plate():
    letters = string.ascii_uppercase + string.digits
    license_plate = "LU " + ''.join(random.choices(letters, k=5))
    return license_plate

# Przykładowe użycie
random_license_plate = generate_license_plate()
print("Wygenerowany numer rejestracyjny: ", random_license_plate)
