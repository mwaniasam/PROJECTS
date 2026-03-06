letters = 'abcdefghijklmnopqrstuvwxyz'

def caesar(text, shift_key, direction):
    result = ''
    if direction == 'decrypt':
        shift_key = -shift_key
    for char in text:
        if char in letters:
            new_position = (letters.index(char) + shift_key) % 26
            result += letters[new_position]
        else:
            result += char
    return result

wanna_use = True
while wanna_use:
    action = input("Type 'encrypt' or 'decrypt':\n").lower()
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if action in ('encrypt', 'decrypt'):
        result = caesar(text=message, shift_key=shift, direction=action)
        print(f"Result: {result}")
    else:
        print(f"'{action}' not recognised. Please type 'encrypt' or 'decrypt'.")

    use_again = input("Type 'yes' to continue, 'no' to exit:\n").lower()
    if use_again == 'no':
        wanna_use = False
        print("Goodbye!")
