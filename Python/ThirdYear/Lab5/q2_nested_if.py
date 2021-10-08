# Lab 5 Q2 (i)

# Determine if candidate is eligible for job - Nested if

years_exp = (int(input("How many years experience do you have in industry? >>> ")))
mcs_cert = input("Do you hold a Microsoft Certification?[y/n] >>> ")
degree_res = input("Do you have a First Class Honors result in a minimum BSc in Computing?[y/n] >>> ")

# Eligible
if years_exp >= 4:
    if mcs_cert == 'y':
        if degree_res == 'y':
            print("You are an eligible candidate!")

# Failed on experience
if years_exp < 4:
    print("You must have 4+ years experience.")

# Failed on Mcs Cert
if years_exp >= 4:
    if mcs_cert == 'n':
        print("You must have a Microsoft Cert.")

# Failed on Degree
if years_exp >= 4:
    if mcs_cert == 'y':
        if degree_res == 'n':
            print("You must have a First Class Honors result in a minimum BSc in Computing.")

