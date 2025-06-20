import random

# Password generation logic


def pass_generate(length, capital_letter, small_letters, special_characters, number):
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    special = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
               ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    result_str = list()

    if capital_letter == "yes":
        for word in upper:
            result_str.append(word)
    if small_letters == "yes":
        for word in lower:
            result_str.append(word)
    if special_characters == "yes":
        for word in special:
            result_str.append(word)
    if number == "yes":
        for word in digits:
            result_str.append(word)
    if len(result_str) == 0:
        print("\n(>_<) Error: No character types selected. Please select at least one character type.")
        return None
    password = ""
    for _ in range(length):
     password += random.choice(result_str)

    print(f"\n          (ง •_•)ง Your Password is: {password}")


# User side interface and choice selection
while True:
    print("\n==========>Password Generator<==========")
    while True:
        try:
            length = int(input("\n----->What's the length of your password: "))
            if length <= 0:
                print("\n(>_<) Length can't be smaller than 1")
            else:
                break
        except ValueError:
            print("\n(>_<) Invalid choice! Type only integers")

    while True:
        capital_letter = input(
            "\n----->Do you want to add capital letters? (YES or NO): ").lower()
        if capital_letter == "yes" or capital_letter == "no":
            break
        else:
            print("\n(>_<) Invalid choice! Type YES or NO")

    while True:
        small_letters = input(
            "\n----->Do you want to add small letters? (YES or NO): ").lower()
        if small_letters == "yes" or small_letters == "no":
            break
        else:
            print("\n(>_<) Invalid choice! Type YES or NO")

    while True:
        special_characters = input(
            "\n----->Do you want to add special characters? (YES or NO): ").lower()
        if special_characters == "yes" or special_characters == "no":
            break
        else:
            print("\n(>_<) Invalid choice! Type YES or NO")
    while True:
        number = input(
            "\n----->Do you want to add Numbers? (YES or NO): ").lower()
        if number == "yes" or number == "no":
            break
        else:
            print("\n(>_<) Invalid choice! Type YES or NO")

    pass_generate(length, capital_letter, small_letters,
                  special_characters, number)

    while True:
        final_choice = input(
            "\n----->Do you want to add Generate more Passwords? (YES or NO): ").lower()
        if final_choice == "yes" or final_choice == "no":
            break
        else:
            print("\n(>_<) Invalid choice! Type YES or NO")

    if final_choice == "yes":
        pass
    else:
        break

print("\n******Thank you for choosing our password generator! Have a nice day*******")