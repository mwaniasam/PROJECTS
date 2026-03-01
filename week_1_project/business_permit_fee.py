"""

Given five kenyan counties, and three business sizes:
Whats the cost of the business permit?
"""

county = input("What's your county of residence(Nairobi, Nakuru, Kisumu, Mombasa, Eldoret)? ").lower()
business_size = input("What's the size of your business(Small, Medium, Large)? ").lower()
permit_fee = None

if county == "nairobi":
    if business_size == "small":
        permit_fee = 10000
    elif business_size == "medium":
        permit_fee = 15000
    elif business_size == "large":
        permit_fee = 20000
    else:
        print("Enter a valid business size!")
elif county == "nakuru":
    if business_size == "small":
        permit_fee = 8000
    elif business_size == "medium":
        permit_fee = 12000
    elif business_size == "large":
        permit_fee = 18000
    else:
        print("Enter a valid business size!")
elif county == "kisumu":
    if business_size == "small":
        permit_fee = 9000
    elif business_size == "medium":
        permit_fee = 14000
    elif business_size == "large":
        permit_fee = 18500
    else:
        print("Enter a valid business size!")
elif county == "mombasa":
    if business_size == "small":
        permit_fee = 9500
    elif business_size == "medium":
        permit_fee = 14500
    elif business_size == "large":
        permit_fee = 19500
    else:
        print("Enter a valid business size!")
elif county == "eldoret":
    if business_size == "small":
        permit_fee = 7000
    elif business_size == "medium":
        permit_fee = 10000
    elif business_size == "large":
        permit_fee = 16500
    else:
        print("Enter a valid business size!")
else:
    print(f"{county.title()} county is not in the given list of counties")

if permit_fee is not None:
    print(f"For a {business_size.title()} size business in {county.title()} county, the permit fee is Ksh {permit_fee:,}.")
