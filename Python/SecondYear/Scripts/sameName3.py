
def chicken():
    global eggs
    eggs = "turkey eggs" # this is global

def bacon():
    eggs = "bacon" # this is local

def ham():
    print(eggs) # this is global
    
eggs = 42 # this is global
chicken()
print(eggs)








