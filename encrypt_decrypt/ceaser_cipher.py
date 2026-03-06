letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(text, shift_key):
    cipher_text = ''
    for char in text:
        if char in letters:
            position = letters.index(char)
            new_position = (position+shift_key) % 26
            cipher_text += letters[new_position]
        else:
            cipher_text += char
    print(f"Your text after encryption is: {cipher_text}")
def decryption(text, shift_key):
    plain_text = ''
    for char in text:
        new_position = None
        if char in letters:
            position = letters.index(char)
            new_position = (position - shift_key)
            if new_position <= 0:
                new_position += 26
                new_position %= 26
            else:
                new_position % 26
        else:
            plain_text += char
        plain_text += letters[new_position]
    print(f"Your cipher text after decryption is: {plain_text}")

wanna_use = True
while wanna_use:
    action = input("Type 'encrypt' for encryption; type 'decrypt' for decryption:\n").lower()
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if action == "encrypt".lower():
        encryption(text=message, shift_key=shift)
    elif action == "decrypt".lower():
        decryption(text=message, shift_key=shift)
    else:
        print(f"{action} not recognised, please choose the right command")
    use_again = input("Type 'yes' to continue, type 'no' to exit.\n").lower()
    if use_again == 'no':
        wanna_use = False
        print("Have a good day! Bye.")
