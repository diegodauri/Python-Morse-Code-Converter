from text import CHARACTERS, MORSE

print("Welcome to the morse converter!")

is_on = True

while is_on:
    user_input = input("Input a text string: ")

    morse_string = []

    for letter in user_input:
        if letter.upper() in CHARACTERS:
            index = CHARACTERS.index(letter.upper())
            morse_string.append(f" {MORSE[index]}")
        else:
            print(f"Invalid character: {letter}")
            break

    print("".join(morse_string))

    y_or_n = input("Convert another string? y/n: ")

    if y_or_n != "y":
        if y_or_n != "Y":
            print("Goodbye!")
            break
    print("\n")