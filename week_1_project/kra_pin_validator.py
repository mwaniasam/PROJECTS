""""
1. Must have 11 characters
2. Starts with a capital letter, either A for individuals or P for non_individuals(enterprises!)
3. Then nine digits
4. Then another capital letter

"""

kra_pin = input("Please enter a valid kra pin: ")
kra_pin = kra_pin.upper()

errors = []

if len(kra_pin) != 11:
    errors.append("KRA pin MUST have 11 characters!")

if kra_pin[0] not in ("A", "P"):
    errors.append("The first character of your pin must be either 'A' or 'P'!")

if not kra_pin[1:10].isdigit():
    errors.append("Characters 1 to 10 must be numbers.")

if not kra_pin[-1].isalpha():
    errors.append("The last character must be a letter.")

if errors:
    print("Invalid pin. Errors found:")
    for error in errors:
        print(f"  - {error}")
else:
    print("Valid KRA pin!")
