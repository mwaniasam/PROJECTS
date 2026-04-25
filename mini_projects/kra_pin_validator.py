""""
1. Must have 11 characters
2. Starts with a capital letter, either A for individuals or P for non_individuals(enterprises!)
3. Then nine digits
4. Then another capital letter

"""
errors = []

def length(kra_pin):
    if len(kra_pin) != 11:
        errors.append("KRA pin MUST have 11 characters!")

def first_char(kra_pin):
    if not kra_pin or kra_pin[0] not in ("A", "P"):
        errors.append("The first character of your pin must be either 'A' or 'P'!")

def digits(kra_pin):
    if len(kra_pin) < 10 or not kra_pin[1:10].isdigit():
        errors.append("Characters 2 to 10 must be numbers.")

def last_char(kra_pin):
    # input already converted to upper so isalpha() check is sufficient
    if not kra_pin or not kra_pin[-1].isalpha():
        errors.append("The last character must be a letter.")

def kra_pin_validator(kra_pin):
    errors.clear()
    length(kra_pin)
    first_char(kra_pin)
    digits(kra_pin)
    last_char(kra_pin)

    if errors:
        print("Invalid KRA PIN:")
        for error in errors:
            print(f"- {error}")
    else:
        print("Valid KRA PIN")

while True:
    kra_pin = input("Enter your KRA PIN: ").upper()
    kra_pin_validator(kra_pin)
    if not errors:
        break

