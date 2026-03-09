# Words commonly found in Kenyan title deeds
title_deed_words = [
    "title", "deed", "parcel", "land", "registered", "proprietor",
    "ownership", "tenure", "freehold", "leasehold",
    "survey", "boundary", "registry", "transfer",
    "encumbrance", "charge", "easement", "allotment"
]

# Words commonly found in Kenyan court judgements
court_judgement_words = [
    "plaintiff", "defendant", "applicant", "respondent",
    "judgement", "ruling", "appeal", "petition",
    "evidence", "affidavit", "testimony", "submission",
    "verdict", "sentence", "jurisdiction", "liability",
    "damages", "order", "decree", "hearing"
]

# Words commonly found in Kenyan business permits
business_permit_words = [
    "permit", "license", "business", "premises",
    "county", "registration", "compliance", "inspection",
    "trading", "fee", "renewal", "tax",
    "authority", "application", "approval",
    "operator", "enterprise", "regulation", "validity"
]
checking = True
while checking:
    word = input("What word do you want to check today?\n").lower()
    if word in title_deed_words:
        print(f"'{word}' suggests this is a Title Deed.")
    elif word in court_judgement_words:
        print(f"'{word}' suggests this is a Court Judgement.")
    elif word in business_permit_words:
        print(f"'{word}' suggests this is a Business Permit.")
    else:
        print(f"'{word}' was not recognised.")

    again = input("Check another word? (yes/no)\n").lower()
    if again == "no":
        checking = False
        print("Goodbye!")

