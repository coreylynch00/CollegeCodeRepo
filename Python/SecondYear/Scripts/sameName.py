
def chicken():
    eggs = "chicken local"
    print(eggs)

def bacon():
    eggs = "bacon local"
    print(eggs)
    chicken()
    print(eggs)

eggs = "global"
bacon()
print(eggs)





