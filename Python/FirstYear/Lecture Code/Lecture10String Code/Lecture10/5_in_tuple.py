county = input("Where are you from? ")

if county == "Cork" or county == "Tipperary" \
        or county == "Kerry"\
        or county == "Waterford" \
        or county=="Clare" or county == "Limerick":
    print("You are from Munster")
else:
    print("You are not from Munster")







munster = ("Cork", "Tipperary", "Kerry",
           "Waterford","Clare", "Limerick")

if county in munster:
    print("You are from Munster")
else:
    print("You are not from Munster")
