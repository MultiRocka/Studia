def caesar_cipher(text, shift):
    encrypted_text = ''.join(map(lambda char: chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else char, text))
    return encrypted_text

# Przykładowe użycie
user_input = input("Podaj tekst do zaszyfrowania (tylko duże litery): ")
shift_amount = int(input("Podaj przesunięcie: "))

encrypted_text = caesar_cipher(user_input, shift_amount)
print("Zaszyfrowany tekst: ", encrypted_text)

