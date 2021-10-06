# Corey Lynch 20/10/2019

user_word = input("Please enter a word.")

print(f"Is this string all uppercase? {user_word.isupper()}")
print(f"Is this string only digits? {user_word.isdigit()}")
print(f"Is this string alphanumeric? {user_word.isalnum()}")
print(f"Does this string begin with a 'c'? {user_word.startswith('c')}")
print(f"Does this string end in 'xxx'? {user_word.endswith('xxx')}")
