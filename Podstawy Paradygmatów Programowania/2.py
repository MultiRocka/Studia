def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    text = text.replace(" ", "")
    reversed_text = reverse_text(text)
    return text == reversed_text

# Przykładowe użycie
user_input = input("Podaj tekst: ")
print("Odwrócny tekst:", reverse_text(user_input))
if is_palindrome(user_input):
    print("Podany tekst jest palindromem.")
else:
    print("Podany tekst nie jest palindromem.")
