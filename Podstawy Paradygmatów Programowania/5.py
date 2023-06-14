
def roman_to_arabic(number):
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    arab_num=0
    for i in range(len(number)):
        if i>0 and roman_dict[number[i]]<roman_dict[number[i-1]]:
            arab_num += roman_dict[number[i]]
        else:
            arab_num += roman_dict[number[i]]-roman_dict[number[i-1]]

    return arab_num

user=input("Podaj liczbe rzymską: ")
arabic_result = roman_to_arabic(user)
print("Liczba w systemie arabskim: ", arabic_result)

# def roman_to_arabic(roman_number):
#     roman_dict = {
#         'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
#     }
#     arabic_number = 0
#
#     for i in range(len(roman_number)):
#         if i > 0 and roman_dict[roman_number[i]] > roman_dict[roman_number[i - 1]]:
#             arabic_number += roman_dict[roman_number[i]] - 2 * roman_dict[roman_number[i - 1]]
#         else:
#             arabic_number += roman_dict[roman_number[i]]
#
#     return arabic_number
#
#
# # Przykładowe użycie
# user_input = input("Podaj liczbę w postaci rzymskiej: ")
# arabic_result = roman_to_arabic(user_input)
# print("Liczba w systemie arabskim: ", arabic_result)
