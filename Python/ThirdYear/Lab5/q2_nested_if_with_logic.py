# Lab 5 Q2 (ii)

# Determine if candidate is eligible for job - single if with logic ops

years_exp = (int(input("How many years experience do you have in industry? >>> ")))
mcs_cert = input("Do you hold a Microsoft Certification?[y/n] >>> ")
degree_res = input("Do you have a First Class Honors result in a minimum BSc in Computing?[y/n] >>> ")

if years_exp >= 4 and mcs_cert == 'y' and degree_res == 'y':
    print("You are eligible!")
else:
    print("You are not eligible!")
