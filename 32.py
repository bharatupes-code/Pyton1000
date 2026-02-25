#Check alphabet, digit or special character.
ch =input("Enter a character:")
if len(ch) !=1:
    print("please enter a single character")
elif ch.isalpha():
    print("It is a alphabet")
elif ch.isdigit():
    print("It is a digit")
else:
    print("It is a special charcter")
