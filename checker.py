import re
password = input("Enter password: ")
if len(password)< 8:
    print("Weak: too short")
elif not re.search("[a-z]", password):
    print("Weak: Add lowercase letters")
elif not re.search("[A-Z]", password):
    print("Weak: Add uppercase letters")
elif not re.search("[0-9]", password):
    print("Weak: Add numbers")
else:
    print("Strong password")
